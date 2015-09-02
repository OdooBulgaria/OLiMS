""" An AnalysisRequest report, containing the report itself in pdf and html
    format. Also, includes information about the date when was published, from
    who, the report recipients (and their emails) and the publication mode
"""
from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import RecordsField
from dependencies import atapi
from dependencies.dependency import ReferenceField, FileField, \
        StringField, Schema, BaseFolder
from dependencies.dependency import BlobField
from dependencies.dependency import HoldingReference
from lims.config import PROJECTNAME
from lims.content.bikaschema import BikaSchema

schema = BikaSchema.copy() + Schema((
    ReferenceField('AnalysisRequest',
       allowed_types=('AnalysisRequest',),
       relationship='ReportAnalysisRequest',
       referenceClass=HoldingReference,
       required=1,
    ),
    BlobField('Pdf',
    ),
    StringField('Html',
    ),
    StringField('SMS',
    ),
    RecordsField('Recipients',
        type='recipients',
        subfields=('UID', 'Username', 'Fullname', 'EmailAddress',
                   'PublicationModes'),
    ),
))

schema['id'].required = False
schema['title'].required = False


class ARReport(BaseFolder):
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

atapi.registerType(ARReport, PROJECTNAME)
