"""AttachmentType - the type of attachment
"""
from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import *
from lims.content.bikaschema import BikaSchema
from lims.config import PROJECTNAME
import sys
from lims import bikaMessageFactory as _
from lims.utils import t
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
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(AttachmentType, PROJECTNAME)
