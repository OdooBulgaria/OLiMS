"""The contact person at a reference supplier organisation.
"""
from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import manage_users
from dependencies.dependency import *
from bika.lims.content.person import Person
from dependencies.dependency import permissions
from dependencies.dependency import getToolByName
from bika.lims.config import PROJECTNAME
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import t
from dependencies.dependency import implements

schema = Person.schema.copy()

schema['JobTitle'].schemata = 'default'
schema['Department'].schemata = 'default'

schema['id'].schemata = 'default'
schema['id'].widget.visible = False
# Don't make title required - it will be computed from the Person's
# Fullname
schema['title'].schemata = 'default'
schema['title'].required = 0
schema['title'].widget.visible = False

class SupplierContact(Person):
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from bika.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(SupplierContact, PROJECTNAME)
