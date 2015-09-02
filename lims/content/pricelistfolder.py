"""PricelistFolder is a container for Pricelist instances.
"""
from dependencies.dependency import ClassSecurityInfo
from lims.interfaces import IPricelistFolder
from dependencies import folder
from lims.content.bikaschema import BikaFolderSchema
from lims import PROJECTNAME
from dependencies.dependency import *
from dependencies.dependency import implements
from lims.interfaces import IHaveNoBreadCrumbs

schema = BikaFolderSchema.copy()
IdField = schema['id']
IdField.widget.visible = {'edit': 'hidden', 'view': 'invisible'}
TitleField = schema['title']
TitleField.widget.visible = {'edit': 'hidden', 'view': 'invisible'}


class PricelistFolder(folder.ATFolder):
    implements(IPricelistFolder, IHaveNoBreadCrumbs)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

registerType(PricelistFolder, PROJECTNAME)
