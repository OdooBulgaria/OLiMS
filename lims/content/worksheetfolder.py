"""WorksheetFolder is a container for Worksheet instances.
"""
from dependencies.dependency import schemata
from dependencies import atapi
from dependencies.dependency import permissions
from dependencies.dependency import getToolByName
from lims.config import PROJECTNAME
from lims.interfaces import IWorksheetFolder, IHaveNoBreadCrumbs
from dependencies import folder
from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import implements
from lims import bikaMessageFactory as _
from lims.utils import t

schema = folder.ATFolderSchema.copy()
schema['id'].widget.visible = {'edit':'hidden', 'view': 'invisible'}
schema['title'].widget.visible = {'edit':'hidden', 'view': 'invisible'}

class WorksheetFolder(folder.ATFolder):
    implements(IWorksheetFolder, IHaveNoBreadCrumbs)
    displayContentsTab = False
    schema = schema
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)

atapi.registerType(WorksheetFolder, PROJECTNAME)
