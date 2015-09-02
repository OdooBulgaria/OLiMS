"""SamplesFolder is a fake folder to live in the nav bar.  It has
view from browser/samplesfolder.py wired to it.
"""
from dependencies.dependency import schemata
from dependencies import atapi
from dependencies.dependency import permissions
from dependencies.dependency import getToolByName
from lims.config import PROJECTNAME
from dependencies.dependency import ClassSecurityInfo
from lims.interfaces import ISamplesFolder, IHaveNoBreadCrumbs
from dependencies import folder
from dependencies.dependency import implements
from lims import bikaMessageFactory as _
from lims.utils import t

schema = folder.ATFolderSchema.copy()

class SamplesFolder(folder.ATFolder):
    implements(ISamplesFolder, IHaveNoBreadCrumbs)
    displayContentsTab = False
    schema = schema
    security = ClassSecurityInfo()

schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)

atapi.registerType(SamplesFolder, PROJECTNAME)
