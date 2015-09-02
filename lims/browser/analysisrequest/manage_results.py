from dependencies.dependency import getSecurityManager
from dependencies.dependency import safe_unicode
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.browser.analyses import AnalysesView
from lims.config import POINTS_OF_CAPTURE
from lims.content.analysisrequest import schema as AnalysisRequestSchema
from lims.permissions import *
from lims.browser.analysisrequest import AnalysisRequestViewView
from lims.utils import to_utf8
from lims.workflow import doActionFor
from dependencies.dependency import DateTime
from dependencies.dependency import PloneMessageFactory as PMF
from dependencies.dependency import IViewView
from dependencies.dependency import getToolByName
from dependencies.dependency import ViewPageTemplateFile
from dependencies.dependency import implements


class AnalysisRequestManageResultsView(AnalysisRequestViewView):
    implements(IViewView)
    template = ViewPageTemplateFile("templates/analysisrequest_manage_results.pt")

    def __call__(self):
        ar = self.context
        workflow = getToolByName(ar, 'portal_workflow')
        if workflow.getInfoFor(ar, 'cancellation_state') == "cancelled":
            self.request.response.redirect(ar.absolute_url())
        elif not(getSecurityManager().checkPermission(EditResults, ar)):
            self.request.response.redirect(ar.absolute_url())
        else:
            self.tables = {}
            show_cats = self.context.bika_setup.getCategoriseAnalysisServices()
            for poc in POINTS_OF_CAPTURE:
                if self.context.getAnalyses(getPointOfCapture=poc):
                    t = self.createAnalysesView(ar,
                                     self.request,
                                     getPointOfCapture=poc,
                                     sort_on='getServiceTitle',
                                     show_categories=show_cats)
                    t.form_id = "ar_manage_results_%s" % poc
                    t.allow_edit = True
                    t.review_states[0]['transitions'] = [{'id': 'submit'},
                                                         {'id': 'retract'},
                                                         {'id': 'verify'}]
                    t.show_select_column = True
                    poc_value = POINTS_OF_CAPTURE.getValue(poc)
                    self.tables[poc_value] = t.contents_table()
            # If a general retracted is done, rise a waring
            if workflow.getInfoFor(ar, 'review_state') == 'sample_received':
                allstatus = list()
                for analysis in ar.getAnalyses():
                    status = workflow.getInfoFor(analysis.getObject(), 'review_state')
                    if status not in ['retracted','to_be_verified','verified']:
                        allstatus = []
                        break
                    else:
                        allstatus.append(status)
                if len(allstatus) > 0:
                    message = "General Retract Done"
                    self.context.plone_utils.addPortalMessage(message, 'warning')

            self.checkInstrumentsValidity()
            return self.template()

    def createAnalysesView(self, context, request, **kwargs):
        return AnalysesView(context, request, **kwargs)

    def checkInstrumentsValidity(self):
        """ Checks the validity of the instruments used in the Analyses
            If an analysis with an invalid instrument (out-of-date or
            with calibration tests failed) is found, a warn message
            will be displayed.
        """
        invalid = []
        ans = [a.getObject() for a in self.context.getAnalyses()]
        for an in ans:
            valid = an.isInstrumentValid()
            if not valid:
                inv = '%s (%s)' % (safe_unicode(an.Title()), safe_unicode(an.getInstrument().Title()))
                if inv not in invalid:
                    invalid.append(inv)
        if len(invalid) > 0:
            message = _("Some analyses use out-of-date or uncalibrated "
                        "instruments. Results edition not allowed")
            message = "%s: %s" % (message, (', '.join(invalid)))
            self.context.plone_utils.addPortalMessage(message, 'warn')
