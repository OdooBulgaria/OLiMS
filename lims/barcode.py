from dependencies.dependency import getToolByName
from lims.browser import BrowserView
from lims import bikaMessageFactory as _
from lims.utils import t
from lims import interfaces
from lims import logger
from lims.permissions import EditResults, EditWorksheet
from dependencies.dependency import check as CheckAuthenticator
from dependencies.dependency import postonly as PostOnly

class barcode_entry(BrowserView):
    """ return redirect url if the item exists
        passes the request to catalog
    """
    def __call__(self):
        try:
            CheckAuthenticator(self.request)
            PostOnly(self.request)
        except:
            return ""

        mtool = getToolByName(self.context, 'portal_membership')
        uc = getToolByName(self.context, 'uid_catalog')
        entry = self.request.get("entry", '').replace("*", "")

        items = uc(UID=entry)
        if not items:
            return ""
        item = items[0].getObject()

        if item.portal_type == "AnalysisRequest":
            if mtool.checkPermission(EditResults, item):
                destination_url = item.absolute_url() + "/manage_results"
            else:
                destination_url = item.absolute_url()
            return self.request.response.redirect(destination_url)

        elif item.portal_type == "Sample":
            ars = item.getAnalysisRequests()
            if len(ars) == 1:
                # If there's only one AR, go there
                if mtool.checkPermission(EditResults, ars[0]):
                    destination_url = ars[0].absolute_url() + "/manage_results"
                else:
                    destination_url = ars[0].absolute_url()
                return self.request.response.redirect(destination_url)
            else:
                # multiple or no ARs: direct to sample.
                destination_url = item.absolute_url()
                return self.request.response.redirect(destination_url)

        elif item.portal_type == "Worksheet":
            if mtool.checkPermission(EditWorksheet, item):
                destination_url = item.absolute_url()
                return self.request.response.redirect(destination_url)

        elif item.portal_type == "ReferenceSample":
            destination_url = item.absolute_url()
            return self.request.response.redirect(destination_url)


"""
Sample round/COC the user lands on the sampling round's view, if he/she is\
authorised to see it
"""
