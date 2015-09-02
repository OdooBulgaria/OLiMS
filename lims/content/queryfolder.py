"""
"""
from dependencies.dependency import ClassSecurityInfo
from lims.config import PROJECTNAME
from lims.interfaces import IQueryFolder, IHaveNoBreadCrumbs
from dependencies import folder
from dependencies import atapi
from dependencies.dependency import schemata
from dependencies.dependency import implements

schema = folder.ATFolderSchema.copy()


class QueryFolder(folder.ATFolder):
    implements(IQueryFolder, IHaveNoBreadCrumbs)
    schema = schema
    displayContentsTab = False
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)

atapi.registerType(QueryFolder, PROJECTNAME)
