from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import *
from dependencies.dependency import HoldingReference
from dependencies.dependency import RecordsField as RecordsField
from lims.browser.widgets import RecordsWidget
from lims.content.bikaschema import BikaSchema
from lims.config import PROJECTNAME
import sys
from lims import bikaMessageFactory as _
from lims.utils import t
from dependencies.dependency import implements

schema = BikaSchema.copy() + Schema((

))

schema['description'].schemata = 'default'
schema['description'].widget.visible = True

class SamplingDeviation(BaseFolder):
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(SamplingDeviation, PROJECTNAME)
