from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import BaseFolder
from dependencies.dependency import DisplayList
from dependencies.dependency import Schema
from dependencies.dependency import registerType
from dependencies.dependency import getToolByName
from lims.config import PROJECTNAME
from lims.content.bikaschema import BikaSchema

schema = BikaSchema.copy() + Schema((

))

schema['description'].schemata = 'default'
schema['description'].widget.visible = True


class SampleCondition(BaseFolder):
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(SampleCondition, PROJECTNAME)


def SampleConditions(self, instance=None, allow_blank=False):
    instance = instance or self
    bsc = getToolByName(instance, 'bika_setup_catalog')
    items = []
    for sm in bsc(portal_type='SampleCondition',
                  inactive_state='active',
                  sort_on='sortable_title'):
        items.append((sm.UID, sm.Title))
    items = allow_blank and [['', '']] + list(items) or list(items)
    return DisplayList(items)
