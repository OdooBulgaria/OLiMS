from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import BaseContent
from dependencies.dependency import registerType
from bika.lims.content.bikaschema import BikaSchema
from bika.lims.config import PROJECTNAME

schema = BikaSchema.copy()
schema['description'].widget.visible = False
schema['description'].schemata = 'default'

class BatchLabel(BaseContent):
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from bika.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(BatchLabel, PROJECTNAME)

