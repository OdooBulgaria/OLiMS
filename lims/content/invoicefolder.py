from dependencies.dependency import ClassSecurityInfo
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.config import ManageInvoices, PROJECTNAME
from lims.interfaces import IInvoiceFolder, IHaveNoBreadCrumbs
from dependencies import atapi
from dependencies.dependency import *
from dependencies import folder
from dependencies.dependency import schemata
from dependencies.dependency import permissions
from dependencies.dependency import UniqueObject
from dependencies.dependency import ConflictError
from dependencies.dependency import implements

schema = folder.ATFolderSchema.copy()
schema['id'].widget.visible = {'edit':'hidden', 'view':'invisible'}
schema['title'].widget.visible = {'edit':'hidden', 'view':'invisible'}


class InvoiceFolder(folder.ATFolder):
    implements(IInvoiceFolder, IHaveNoBreadCrumbs)
    displayContentsTab = False
    schema = schema
    security = ClassSecurityInfo()


atapi.registerType(InvoiceFolder, PROJECTNAME)
