from dependencies.dependency import ClassSecurityInfo
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import t
from bika.lims.config import ManageInvoices, PROJECTNAME
from bika.lims.interfaces import IInvoiceFolder, IHaveNoBreadCrumbs
from dependencies.dependency import atapi
from dependencies.dependency import *
from dependencies.dependency import folder
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
