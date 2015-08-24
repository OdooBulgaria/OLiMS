"""PricelistFolder is a container for Pricelist instances.
"""
from dependencies.dependency import ClassSecurityInfo
from bika.lims.interfaces import IPricelistFolder
from dependencies.dependency import folder
from bika.lims.content.bikaschema import BikaFolderSchema
from bika.lims import PROJECTNAME
from dependencies.dependency import *
from dependencies.dependency import implements
from bika.lims.interfaces import IHaveNoBreadCrumbs

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
