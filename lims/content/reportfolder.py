from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import *
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims.interfaces import IReportFolder, IHaveNoBreadCrumbs
from OLiMS.dependencies.folder import ATFolder, ATFolderSchema
from OLiMS.dependencies.dependency import implements

schema = ATFolderSchema.copy()

class ReportFolder(ATFolder):
    implements(IReportFolder, IHaveNoBreadCrumbs)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

registerType(ReportFolder, PROJECTNAME)
