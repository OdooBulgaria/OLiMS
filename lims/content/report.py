from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies.dependency import atapi
from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import DateTime
from OLiMS.dependencies.dependency import DateTimeField, DateTimeWidget
from OLiMS.dependencies.dependency import REFERENCE_CATALOG
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import ListFolderContents, View
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims.content.bikaschema import BikaSchema
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.dependencies.dependency import implements

schema = BikaSchema.copy() + Schema((
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
    ReferenceField('Client',
        allowed_types = ('Client',),
        relationship = 'ReportClient',
        widget = ReferenceWidget(
            label=_("Client"),
        ),
    ),
    ComputedField('ClientUID',
        expression = 'here.getClient() and here.getClient().UID()',
        widget = ComputedWidget(
            visible = False,
        ),
    ),
),
)

schema['id'].required = False
schema['title'].required = False

class Report(BaseFolder):
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from OLiMS.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    security.declarePublic('current_date')
    def current_date(self):
        """ return current date """
        return DateTime()


atapi.registerType(Report, PROJECTNAME)
