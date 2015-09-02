from dependencies.dependency import ClassSecurityInfo
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.config import PROJECTNAME
from lims.interfaces import ISubGroups
from lims import bikaMessageFactory as _b
from lims.browser.bika_listing import BikaListingView
from dependencies.dependency import IFolderContentsView
from dependencies.folder import ATFolderSchema, ATFolder
from dependencies.dependency import IViewView
from dependencies import atapi
from dependencies.dependency import schemata
from dependencies.dependency import getToolByName
from dependencies.dependency import implements


class SubGroupsView(BikaListingView):
    implements(IFolderContentsView, IViewView)

    def __init__(self, context, request):
        super(SubGroupsView, self).__init__(context, request)
        self.catalog = 'bika_setup_catalog'
        self.contentFilter = {'portal_type': 'SubGroup',
                              'sort_on': 'sortable_title'}
        self.context_actions = {
            _('Add'): {
                'url': 'createObject?type_name=SubGroup',
                'icon': '++resource++bika.lims.images/add.png'
            }
        }
        self.icon = self.portal_url + \
            "/++resource++bika.lims.images/batch_big.png"
        self.title = self.context.translate(_("Sub-groups"))
        self.description = ""
        self.show_sort_column = False
        self.show_select_row = False
        self.show_select_column = True
        self.pagesize = 25

        self.columns = {
            'Title': {'title': _('Sub-group'),
                      'index': 'sortable_title'},
            'Description': {'title': _('Description'),
                            'index': 'description',
                            'toggle': True},
            'SortKey': {'title': _('Sort Key')},
        }

        self.review_states = [
            {'id': 'default',
             'title': _('Active'),
             'contentFilter': {'inactive_state': 'active'},
             'transitions': [{'id': 'deactivate'}, ],
             'columns': ['Title', 'Description', 'SortKey']},
            {'id': 'inactive',
             'title': _('Inactive'),
             'contentFilter': {'inactive_state': 'inactive'},
             'transitions': [{'id': 'activate'}, ],
             'columns': ['Title', 'Description', 'SortKey']},
            {'id': 'all',
             'title': _('All'),
             'contentFilter': {},
             'columns': ['Title', 'Description', 'SortKey']},
        ]

    def folderitems(self):
        items = BikaListingView.folderitems(self)
        for x in range(len(items)):
            if 'obj' not in items[x]:
                continue
            obj = items[x]['obj']
            items[x]['Description'] = obj.Description()
            items[x]['replace']['Title'] = "<a href='%s'>%s</a>" % \
                (items[x]['url'], items[x]['Title'])

        return items

schema = ATFolderSchema.copy()


class SubGroups(ATFolder):
    implements(ISubGroups)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)
atapi.registerType(SubGroups, PROJECTNAME)
