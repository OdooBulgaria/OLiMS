from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import *
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.config import PROJECTNAME
from lims.interfaces import IReportFolder, IHaveNoBreadCrumbs
from dependencies.folder import ATFolder, ATFolderSchema
from dependencies.dependency import implements

schema = ATFolderSchema.copy()

class ReportFolder(ATFolder):
    implements(IReportFolder, IHaveNoBreadCrumbs)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

registerType(ReportFolder, PROJECTNAME)
