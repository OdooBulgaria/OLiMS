from bika.lims.utils import isActive
"""ClientFolder is a container for Client instances.
"""
from dependencies.dependency import schemata
from dependencies.dependency import atapi
from dependencies.dependency import permissions
from dependencies.dependency import DisplayList
from dependencies.dependency import getToolByName
from bika.lims.config import PROJECTNAME
from dependencies.dependency import ClassSecurityInfo
from bika.lims.interfaces import IClientFolder, IHaveNoBreadCrumbs
from dependencies.dependency import folder
from dependencies.dependency import implements
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import t

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
