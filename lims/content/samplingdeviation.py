from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import HoldingReference
from OLiMS.dependencies.dependency import RecordsField as RecordsField
from OLiMS.lims.browser.widgets import RecordsWidget
from OLiMS.lims.content.bikaschema import BikaSchema
from OLiMS.lims.config import PROJECTNAME
import sys
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.dependencies.dependency import implements

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
        from OLiMS.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(SamplingDeviation, PROJECTNAME)
