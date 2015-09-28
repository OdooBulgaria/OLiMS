# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import schemata
# from dependencies import atapi
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import DateTime
# from dependencies.dependency import DateTimeField, DateTimeWidget
# from dependencies.dependency import REFERENCE_CATALOG
# from dependencies.dependency import *
# from dependencies.dependency import ListFolderContents, View
# from dependencies.dependency import getToolByName
# from lims.content.bikaschema import BikaSchema
# from lims.config import PROJECTNAME
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from dependencies.dependency import implements

from lims import bikaMessageFactory as _
from fields.string_field import StringField

from fields.file_field import FileField
from fields.widget.widget import StringWidget, FileWidget
from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel



#schema = BikaSchema.copy() + Schema((
schema = (
             FileField('ReportFile',
            widget = FileWidget(
            label=_("Report"),
        ),
    ),
    StringField('ReportType',
        widget = StringWidget(
            label=_("Report Type"),
            description=_("Report type"),
        ),
    ),

    fields.Many2one(string='Client',
                   comodel_name='olims.client',
#             allowed_types = ('Client',),
#         relationship = 'ReportClient',
#         widget = ReferenceWidget(
#             label=_("Client"),
#         ),
                    ),

# ~~~~~~~ To be implemented ~~~~~~~
    # ComputedField('ClientUID',
    #     expression = 'here.getClient() and here.getClient().UID()',
    #     widget = ComputedWidget(
    #         visible = False,
    #     ),
    # ),
)


# schema['id'].required = False
# schema['title'].required = False

class Report(models.Model, BaseOLiMSModel): #BaseFolder
    _name ='olims.report'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    #security.declarePublic('current_date')
    def current_date(self):
        """ return current date """
        return DateTime()


#atapi.registerType(Report, PROJECTNAME)
Report.initialze(schema)