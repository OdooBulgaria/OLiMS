from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import *
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import t
from bika.lims.config import PROJECTNAME
from bika.lims.interfaces import IReportFolder, IHaveNoBreadCrumbs
from dependencies.dependency import ATFolder, ATFolderSchema
from dependencies.dependency import implements

schema = ATFolderSchema.copy()

class ReportFolder(ATFolder):
    implements(IReportFolder, IHaveNoBreadCrumbs)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

registerType(ReportFolder, PROJECTNAME)
