from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import *
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.config import PROJECTNAME
from lims.content.bikaschema import BikaSchema
from lims.interfaces import IManufacturer
from dependencies.dependency import implements

schema = BikaSchema.copy()

schema['description'].schemata = 'default'
schema['description'].widget.visible = True

class Manufacturer(BaseContent):
    implements(IManufacturer)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(Manufacturer, PROJECTNAME)
