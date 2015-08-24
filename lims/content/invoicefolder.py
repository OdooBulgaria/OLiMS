from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.config import ManageInvoices, PROJECTNAME
from OLiMS.lims.interfaces import IInvoiceFolder, IHaveNoBreadCrumbs
from OLiMS.dependencies.dependency import atapi
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import folder
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies.dependency import permissions
from OLiMS.dependencies.dependency import UniqueObject
from OLiMS.dependencies.dependency import ConflictError
from OLiMS.dependencies.dependency import implements

schema = folder.ATFolderSchema.copy()
schema['id'].widget.visible = {'edit':'hidden', 'view':'invisible'}
schema['title'].widget.visible = {'edit':'hidden', 'view':'invisible'}


class InvoiceFolder(folder.ATFolder):
    implements(IInvoiceFolder, IHaveNoBreadCrumbs)
    displayContentsTab = False
    schema = schema
    security = ClassSecurityInfo()


atapi.registerType(InvoiceFolder, PROJECTNAME)
