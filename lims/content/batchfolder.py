from lims.utils import isActive
"""BatchFolder contains AR Batches.
"""
from dependencies.dependency import schemata
from dependencies import atapi
from dependencies.dependency import DisplayList
from dependencies.dependency import permissions
from dependencies.dependency import getToolByName
from lims.config import PROJECTNAME
from dependencies.dependency import ClassSecurityInfo
from lims.interfaces import IBatchFolder, IHaveNoBreadCrumbs
from dependencies import folder
from dependencies.dependency import implements
from lims import bikaMessageFactory as _
from lims.utils import t
import json

schema = folder.ATFolderSchema.copy()


class BatchFolder(folder.ATFolder):
    implements(IBatchFolder, IHaveNoBreadCrumbs)
    schema = schema
    displayContentsTab = False
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)

atapi.registerType(BatchFolder, PROJECTNAME)
