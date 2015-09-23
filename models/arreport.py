""" An AnalysisRequest report, containing the report itself in pdf and html
    format. Also, includes information about the date when was published, from
    who, the report recipients (and their emails) and the publication mode
# """
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import RecordsField
# from dependencies import atapi
# from dependencies.dependency import ReferenceField, FileField, \
#         StringField, Schema, BaseFolder
# from dependencies.dependency import BlobField
# from dependencies.dependency import HoldingReference
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema

#schema = BikaSchema.copy() + Schema((

from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
# from fields.widget.widget import StringWidget
# from lims import bikaMessageFactory as _


schema = (
        fields.Many2one(string='AnalysisRequest',
                    comodel_name='olims.analysis_request',

    ),

    #    ReferenceField('AnalysisRequest',
    #    allowed_types=('AnalysisRequest',),
    #    relationship='ReportAnalysisRequest',
    #    referenceClass=HoldingReference,
    #    required=1,
    # ),
    fields.Binary(string='Pdf'),
    # BlobField('Pdf',
    # ),
    StringField('Html',
    ),
    StringField('SMS',
    ),
    # ~~~~~~~ To be implemented ~~~~~~~
    # RecordsField('Recipients',
    #     type='recipients',
    #     subfields=('UID', 'Username', 'Fullname', 'EmailAddress',
    #                'PublicationModes'),
    # ),
)

# schema['id'].required = False
# schema['title'].required = False


class ARReport(models.Model, BaseOLiMSModel): #BaseFolder
    _name='olims.ar_report'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

#atapi.registerType(ARReport, PROJECTNAME)
ARReport.initialze(schema)