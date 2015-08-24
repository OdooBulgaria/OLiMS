"""Supply Order Folder contains Supply Orders
"""
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies.dependency import atapi
from OLiMS.lims.config import PROJECTNAME
from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.lims.interfaces import ISupplyOrderFolder, IHaveNoBreadCrumbs
from OLiMS.dependencies.dependency import folder
from OLiMS.dependencies.dependency import implements

schema = folder.ATFolderSchema.copy()


class SupplyOrderFolder(folder.ATFolder):
    implements(ISupplyOrderFolder, IHaveNoBreadCrumbs)
    schema = schema
    displayContentsTab = False
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)

atapi.registerType(SupplyOrderFolder, PROJECTNAME)
