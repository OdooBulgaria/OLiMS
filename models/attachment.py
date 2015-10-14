# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import schemata
# from dependencies import atapi
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import DateTime
# from dependencies.dependency import DateTimeField, DateTimeWidget, RecordsField
# from dependencies.dependency import REFERENCE_CATALOG
# from dependencies.dependency import *
# from dependencies.dependency import ListFolderContents, View
# from dependencies.dependency import getToolByName
# from dependencies.dependency import safe_unicode
# from lims.content.bikaschema import BikaSchema
# from lims.config import PROJECTNAME
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from dependencies.dependency import implements

from openerp import fields, models
from fields.string_field import StringField
from fields.date_time_field import DateTimeField
from fields.file_field import FileField
from fields.widget.widget import  DateTimeWidget, FileWidget, StringWidget
from models.base_olims_model import BaseOLiMSModel
from lims import bikaMessageFactory as _



#schema = BikaSchema.copy() + Schema((
schema = (
    # ~~~~~~~ To be implemented ~~~~~~~
    #          ComputedField('RequestID',
    #     expression = 'here.getRequestID()',
    #     widget = ComputedWidget(
    #         visible = True,
    #     ),
    # ),
    FileField('AttachmentFile',
        widget = FileWidget(
            label=_("Attachment"),
        ),
    ),


    fields.Many2one(string='AttachmentType',
                    comodel_name='olims.attachment_type',
                    required=False,
                    help='Attachment Type'

        #   required = 0,
        # allowed_types = ('AttachmentType',),
        # relationship = 'AttachmentAttachmentType',
        # widget = ReferenceWidget(
        #     label=_("Attachment Type"),
        # ),
        ),

     StringField('AttachmentKeys',
        searchable = True,
        widget = StringWidget(
            label=_("Attachment Keys"),
        ),
    ),
    DateTimeField('DateLoaded',
        required = 1,
        default_method = 'current_date',
        widget = DateTimeWidget(
            label=_("Date Loaded"),
        ),
    ),
    # ~~~~~~~ To be implemented ~~~~~~~
    # ComputedField('AttachmentTypeUID',
    #     expression="context.getAttachmentType().UID() if context.getAttachmentType() else ''",
    #     widget = ComputedWidget(
    #         visible = False,
    #     ),
    # ),
    # ComputedField('ClientUID',
    #     expression = 'here.aq_parent.UID()',
    #     widget = ComputedWidget(
    #         visible = False,
    #     ),
    # ),
)

# schema['id'].required = False
# schema['title'].required = False

class Attachment(models.Model, BaseOLiMSModel): #BaseFolder
    _name='olims.attachment'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def Title(self):
        """ Return the Id """
        return safe_unicode(self.getId()).encode('utf-8')

    def getTextTitle(self):
        """ Return the request and possibly analayis title as title """
        requestid = self.getRequestID()
        if requestid:
            analysis = self.getAnalysis()
            if analysis:
                return '%s - %s' % (requestid, analysis.Title())
            else:
                return requestid
        else:
            return None

    def getRequest(self):
        """ Return the AR to which this is linked """
        """ there is a short time between creation and linking """
        """ when it is not linked """
        tool = getToolByName(self, REFERENCE_CATALOG)
        uids = [uid for uid in
                tool.getBackReferences(self, 'AnalysisRequestAttachment')]
        if len(uids) == 1:
            reference = uids[0]
            ar = tool.lookupObject(reference.sourceUID)
            return ar
        else:
            uids = [uid for uid in
                    tool.getBackReferences(self, 'AnalysisAttachment')]
            if len(uids) == 1:
                reference = uids[0]
                analysis = tool.lookupObject(reference.sourceUID)
                ar = analysis.aq_parent
                return ar
        return None

    def getRequestID(self):
        """ Return the ID of the request to which this is linked """
        ar = self.getRequest()
        if ar:
            return ar.getRequestID()
        else:
            return None

    def getAnalysis(self):
        """ Return the analysis to which this is linked """
        """  it may not be linked to an analysis """
        tool = getToolByName(self, REFERENCE_CATALOG)
        uids = [uid for uid in
                tool.getBackReferences(self, 'AnalysisAttachment')]
        if len(uids) == 1:
            reference = uids[0]
            analysis = tool.lookupObject(reference.sourceUID)
            return analysis
        return None

    def getParentState(self):
        """ Return the review state of the object - analysis or AR """
        """ to which this is linked """
        tool = getToolByName(self, REFERENCE_CATALOG)
        uids = [uid for uid in
                tool.getBackReferences(self, 'AnalysisAttachment')]
        if len(uids) == 1:
            reference = uids[0]
            parent = tool.lookupObject(reference.sourceUID)
        else:
            uids = [uid for uid in
                    tool.getBackReferences(self, 'AnalysisRequestAttachment')]
            if len(uids) == 1:
                reference = uids[0]
                parent = tool.lookupObject(reference.sourceUID)
        workflow = getToolByName(self, 'portal_workflow')
        return workflow.getInfoFor(parent, 'review_state', '')

    #security.declarePublic('current_date')
    def current_date(self):
        """ return current date """
        return DateTime()


#atapi.registerType(Attachment, PROJECTNAME)
Attachment.initialze(schema)