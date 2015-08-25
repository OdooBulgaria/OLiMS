from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import HoldingReference
from OLiMS.dependencies.dependency import RecordsField as RecordsField
from OLiMS.dependencies.dependency import getToolByName
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

class SampleMatrix(BaseFolder):
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from OLiMS.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(SampleMatrix, PROJECTNAME)

def SampleMatrices(self, instance=None, allow_blank=False):
    instance = instance or self
    bsc = getToolByName(instance, 'bika_setup_catalog')
    items = []
    for sm in bsc(portal_type='SampleMatrix',
                  inactive_state='active',
                  sort_on = 'sortable_title'):
        items.append((sm.UID, sm.Title))
    items = allow_blank and [['','']] + list(items) or list(items)
    return DisplayList(items)
