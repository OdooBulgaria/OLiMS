"""WorksheetFolder is a container for Worksheet instances.
"""
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import permissions
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims.interfaces import IWorksheetFolder, IHaveNoBreadCrumbs
from OLiMS.dependencies import folder
from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import implements
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t

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
