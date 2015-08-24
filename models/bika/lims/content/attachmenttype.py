"""AttachmentType - the type of attachment
"""
from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import *
from dependencies.dependency import ModifyPortalContent
from bika.lims.content.bikaschema import BikaSchema
from bika.lims.config import PROJECTNAME
import sys
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import t
from dependencies.dependency import implements

schema = BikaSchema.copy()

schema['description'].widget.visible = True
schema['description'].schemata = 'default'

class AttachmentType(BaseContent):
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from bika.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(AttachmentType, PROJECTNAME)
