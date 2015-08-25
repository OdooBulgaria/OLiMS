""" An AnalysisRequest report, containing the report itself in pdf and html
    format. Also, includes information about the date when was published, from
    who, the report recipients (and their emails) and the publication mode
"""
from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import RecordsField
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import ReferenceField, FileField, \
        StringField, Schema, BaseFolder
from OLiMS.dependencies.dependency import BlobField
from OLiMS.dependencies.dependency import HoldingReference
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims.content.bikaschema import BikaSchema

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
        from OLiMS.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

atapi.registerType(ARReport, PROJECTNAME)
