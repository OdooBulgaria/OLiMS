"""
"""
from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims.interfaces import IQueryFolder, IHaveNoBreadCrumbs
from OLiMS.dependencies import folder
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies.dependency import implements

schema = folder.ATFolderSchema.copy()


class QueryFolder(folder.ATFolder):
    implements(IQueryFolder, IHaveNoBreadCrumbs)
    schema = schema
    displayContentsTab = False
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)

atapi.registerType(QueryFolder, PROJECTNAME)
