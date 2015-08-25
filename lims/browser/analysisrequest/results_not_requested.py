from OLiMS.dependencies.dependency import getSecurityManager
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.permissions import *
from OLiMS.lims.browser.analysisrequest import AnalysisRequestManageResultsView
from OLiMS.lims.content.analysisrequest import schema as AnalysisRequestSchema
from OLiMS.lims.utils import to_utf8
from OLiMS.lims.workflow import doActionFor
from OLiMS.dependencies.dependency import IViewView
from OLiMS.dependencies.dependency import DateTime
from OLiMS.dependencies.dependency import PloneMessageFactory as PMF
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.dependencies.dependency import ViewPageTemplateFile
from OLiMS.dependencies.dependency import implements


class AnalysisRequestResultsNotRequestedView(AnalysisRequestManageResultsView):
    implements(IViewView)
    template = ViewPageTemplateFile("templates/analysisrequest_analyses_not_requested.pt")

    def __call__(self):
        ar = self.context
        workflow = getToolByName(ar, 'portal_workflow')

        # If is a retracted AR, show the link to child AR and show a warn msg
        if workflow.getInfoFor(ar, 'review_state') == 'invalid':
            childar = hasattr(ar, 'getChildAnalysisRequest') \
                        and ar.getChildAnalysisRequest() or None
            childid = childar and childar.getRequestID() or None
            message = _('This Analysis Request has been withdrawn and is shown '
                        'for trace-ability purposes only. Retest: ${retest_child_id}.',
                        mapping={"retest_child_id":childid if childid else ''})
            self.context.plone_utils.addPortalMessage(message, 'warning')

        # If is an AR automatically generated due to a Retraction, show it's
        # parent AR information
        if hasattr(ar, 'getParentAnalysisRequest') \
            and ar.getParentAnalysisRequest():
            par = ar.getParentAnalysisRequest()
            message = _(
                'This Analysis Request has been generated automatically due to '
                'the retraction of the Analysis Request ${retracted_request_id}.',
                mapping={"retracted_request_id": par.getRequestID()})
            self.context.plone_utils.addPortalMessage(message, 'info')

        can_do = getSecurityManager().checkPermission(ResultsNotRequested, ar)
        if workflow.getInfoFor(ar, 'cancellation_state') == "cancelled":
            self.request.response.redirect(ar.absolute_url())
        elif not(can_do):
            self.request.response.redirect(ar.absolute_url())
        else:
            return self.template()
