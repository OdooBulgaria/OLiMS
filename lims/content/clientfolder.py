from OLiMS.lims.utils import isActive
"""ClientFolder is a container for Client instances.
"""
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import permissions
from OLiMS.dependencies.dependency import DisplayList
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims.config import PROJECTNAME
from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.lims.interfaces import IClientFolder, IHaveNoBreadCrumbs
from OLiMS.dependencies import folder
from OLiMS.dependencies.dependency import implements
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t

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
