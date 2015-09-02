"""Supply Order Folder contains Supply Orders
"""
from dependencies.dependency import schemata
from dependencies import atapi
from lims.config import PROJECTNAME
from dependencies.dependency import ClassSecurityInfo
from lims.interfaces import ISupplyOrderFolder, IHaveNoBreadCrumbs
from dependencies import folder
from dependencies.dependency import implements

schema = folder.ATFolderSchema.copy()


class SupplyOrderFolder(folder.ATFolder):
    implements(ISupplyOrderFolder, IHaveNoBreadCrumbs)
    schema = schema
    displayContentsTab = False
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)

atapi.registerType(SupplyOrderFolder, PROJECTNAME)
