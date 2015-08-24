from bika.lims.utils import isActive
"""BatchFolder contains AR Batches.
"""
from dependencies.dependency import schemata
from dependencies.dependency import atapi
from dependencies.dependency import DisplayList
from dependencies.dependency import permissions
from dependencies.dependency import getToolByName
from bika.lims.config import PROJECTNAME
from dependencies.dependency import ClassSecurityInfo
from bika.lims.interfaces import IBatchFolder, IHaveNoBreadCrumbs
from dependencies.dependency import folder
from dependencies.dependency import implements
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import t
import json

schema = folder.ATFolderSchema.copy()


class BatchFolder(folder.ATFolder):
    implements(IBatchFolder, IHaveNoBreadCrumbs)
    schema = schema
    displayContentsTab = False
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)

atapi.registerType(BatchFolder, PROJECTNAME)
