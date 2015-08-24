from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import View, ModifyPortalContent
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims.content.bikaschema import BikaSchema
from OLiMS.lims.interfaces import IInstrumentType
from OLiMS.dependencies.dependency import implements

schema = BikaSchema.copy()

schema['description'].schemata = 'default'
schema['description'].widget.visible = True

class InstrumentType(BaseContent):
    implements(IInstrumentType)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from OLiMS.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(InstrumentType, PROJECTNAME)
