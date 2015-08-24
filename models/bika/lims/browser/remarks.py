from bika.lims.browser import BrowserView
from dependencies.dependency import DateTime
from dependencies.dependency import getSecurityManager
from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import getToolByName
from dependencies.dependency import TextAreaWidget
from dependencies.dependency import registerWidget
import plone

from dependencies.dependency import \
     convertWebIntelligentPlainTextToHtml, \
     convertHtmlToWebIntelligentPlainText

class ajaxSetRemarks(BrowserView):
    """ Modify Remarks field and return new rendered field value
    """
    def __call__(self):
        plone.protect.CheckAuthenticator(self.request)
        field = self.context.Schema()["Remarks"]
        value = self.request['value'].strip() + "\n\n"
        existing = self.context.getRemarks(mimetype='text/x-web-intelligent').strip()

        date = DateTime().rfc822()
        user = getSecurityManager().getUser()
        divider = "=== %s (%s)\n" % (date, user)

        remarks = convertWebIntelligentPlainTextToHtml(divider) + \
            convertWebIntelligentPlainTextToHtml(value) + \
            convertWebIntelligentPlainTextToHtml(existing)

        self.context.setRemarks(divider + value + existing, mimetype='text/x-web-intelligent')

        return remarks.strip()
