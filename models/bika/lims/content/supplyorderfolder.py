"""Supply Order Folder contains Supply Orders
"""
from dependencies.dependency import schemata
from dependencies.dependency import atapi
from bika.lims.config import PROJECTNAME
from dependencies.dependency import ClassSecurityInfo
from bika.lims.interfaces import ISupplyOrderFolder, IHaveNoBreadCrumbs
from dependencies.dependency import folder
from dependencies.dependency import implements

schema = folder.ATFolderSchema.copy()


class SupplyOrderFolder(folder.ATFolder):
    implements(ISupplyOrderFolder, IHaveNoBreadCrumbs)
    schema = schema
    displayContentsTab = False
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)

atapi.registerType(SupplyOrderFolder, PROJECTNAME)
