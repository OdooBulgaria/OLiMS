"""PricelistFolder is a container for Pricelist instances.
"""
from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.lims.interfaces import IPricelistFolder
from OLiMS.dependencies.dependency import folder
from OLiMS.lims.content.bikaschema import BikaFolderSchema
from OLiMS.lims import PROJECTNAME
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import implements
from OLiMS.lims.interfaces import IHaveNoBreadCrumbs

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
