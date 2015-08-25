"""ReferenceSamplesFolder is a fake folder to live in the nav bar.  It has
view from browser/referencesample.py wired to it.
"""
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import permissions
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims.config import PROJECTNAME
from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.lims.interfaces import IReferenceSamplesFolder, IHaveNoBreadCrumbs
from OLiMS.dependencies import folder
from OLiMS.dependencies.dependency import implements
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t

schema = folder.ATFolderSchema.copy()

class ReferenceSamplesFolder(folder.ATFolder):
    implements(IReferenceSamplesFolder, IHaveNoBreadCrumbs)
    displayContentsTab = False
    schema = schema
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)

atapi.registerType(ReferenceSamplesFolder, PROJECTNAME)
