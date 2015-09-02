from lims.utils import isActive
"""ClientFolder is a container for Client instances.
"""
from dependencies.dependency import schemata
from dependencies import atapi
from dependencies.dependency import permissions
from dependencies.dependency import DisplayList
from dependencies.dependency import getToolByName
from lims.config import PROJECTNAME
from dependencies.dependency import ClassSecurityInfo
from lims.interfaces import IClientFolder, IHaveNoBreadCrumbs
from dependencies import folder
from dependencies.dependency import implements
from lims import bikaMessageFactory as _
from lims.utils import t

schema = folder.ATFolderSchema.copy()
schema['id'].widget.visible = {'edit': 'hidden', 'view': 'invisible'}
schema['title'].widget.visible = {'edit': 'hidden', 'view': 'invisible'}


class ClientFolder(folder.ATFolder):
    implements(IClientFolder, IHaveNoBreadCrumbs)
    displayContentsTab = False
    schema = schema
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)

atapi.registerType(ClientFolder, PROJECTNAME)
