from OLiMS.lims.browser import BrowserView
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.dependencies.dependency import getToolByName
import json
from OLiMS.dependencies.dependency import check as CheckAuthenticator

class ajaxDeleteAnalysisAttachment():
    """ Removes an analysis attachment. """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        form = self.request.form
        CheckAuthenticator(self.request.form)
        attachment_uid = form.get('attachment_uid', None)
        if not attachment_uid:
            return "error"
        uc = getToolByName(self.context, 'uid_catalog')
        attachment = uc(UID=attachment_uid)
        if not attachment:
            return "%s does not exist" % attachment_uid
        attachment = attachment[0].getObject()
        for analysis in attachment.getBackReferences("AnalysisAttachment"):
            analysis.setAttachment([r for r in analysis.getAttachment()
                                    if r.UID() != attachment.UID()])
        for analysis in attachment.getBackReferences("DuplicateAnalysisAttachment"):
            analysis.setAttachment([r for r in analysis.getAttachment()
                                    if r.UID() != attachment.UID()])
        attachment.aq_parent.manage_delObjects(ids=[attachment.getId(),])
        return "success"
