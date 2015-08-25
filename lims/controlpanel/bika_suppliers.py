from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import registerType
from OLiMS.dependencies.dependency import permissions
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims.browser import BrowserView
from OLiMS.lims.browser.bika_listing import BikaListingView
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.dependencies.dependency import IViewView
from OLiMS.lims.content.bikaschema import BikaFolderSchema
from OLiMS.dependencies.dependency import IFolderContentsView
from OLiMS.dependencies.folder import ATFolder, ATFolderSchema
from OLiMS.lims.interfaces import ISuppliers
from OLiMS.dependencies.dependency import implements

class SuppliersView(BikaListingView):
    implements(IFolderContentsView, IViewView)
    def __init__(self, context, request):
        super(SuppliersView, self).__init__(context, request)
        self.catalog = 'bika_setup_catalog'
        self.contentFilter = {'portal_type': 'Supplier', 
                              'sort_on': 'sortable_title'}
        self.context_actions = {_('Add'):
                                {'url': 'createObject?type_name=Supplier',
                                 'icon': '++resource++bika.lims.images/add.png'}}
        self.title = self.context.translate(_("Suppliers"))
        self.icon = "++resource++bika.lims.images/supplier_big.png"
        self.description = ""
        self.show_sort_column = False
        self.show_select_row = False
        self.show_select_column = True
        self.pagesize = 25

        self.columns = {
            'Name': {'title': _('Name'),
                     'index': 'getName'},
            'Email': {'title': _('Email'),
                      'toggle': True},
            'Phone': {'title': _('Phone'),
                      'toggle': True},
            'Fax': {'title': _('Fax'),
                    'toggle': True},
        }
        self.review_states = [
            {'id':'default',
             'title': _('Active'),
             'contentFilter': {'inactive_state': 'active'},
             'transitions': [{'id':'deactivate'}, ],
             'columns': ['Name', 'Email', 'Phone', 'Fax']},
            {'id':'inactive',
             'title': _('Dormant'),
             'contentFilter': {'inactive_state': 'inactive'},
             'transitions': [{'id':'activate'}, ],
             'columns': ['Name', 'Email', 'Phone', 'Fax']},
            {'id':'all',
             'title': _('All'),
             'contentFilter':{},
             'columns': ['Name', 'Email', 'Phone', 'Fax']},
        ]

    def folderitems(self):
        items = BikaListingView.folderitems(self)
        for x in range(len(items)):
            if not items[x].has_key('obj'): continue
            obj = items[x]['obj']
            items[x]['Name'] = obj.getName()
            items[x]['Email'] = obj.getEmailAddress()
            items[x]['Phone'] = obj.getPhone()
            items[x]['Fax'] = obj.getFax()
            items[x]['replace']['Name'] = "<a href='%s'>%s</a>" % \
                 (items[x]['url'], items[x]['Name'])

        return items

schema = ATFolderSchema.copy()
class Suppliers(ATFolder):
    implements(ISuppliers)
    displayContentsTab = False
    schema = schema

schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)
atapi.registerType(Suppliers, PROJECTNAME)
