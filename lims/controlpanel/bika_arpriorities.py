from OLiMS.lims.browser.bika_listing import BikaListingView
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.interfaces import IARPriorities
from OLiMS.dependencies.dependency import IViewView
from OLiMS.dependencies.dependency import IFolderContentsView
from OLiMS.dependencies.folder import ATFolder, ATFolderSchema
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import implements


class ARPrioritiesView(BikaListingView):
    implements(IFolderContentsView, IViewView)

    def __init__(self, context, request):
        super(ARPrioritiesView, self).__init__(context, request)
        request.set('disable_plone.rightcolumn', 1)

        self.catalog = 'bika_setup_catalog'
        self.contentFilter = {
                'portal_type': 'ARPriority',
                'path': {'query': '/'.join(context.getPhysicalPath())},
                'sort_on': 'sortKey',
                }
        self.context_actions[_('Add')] = \
                {'url': 'createObject?type_name=ARPriority',
                 'icon': self.portal.absolute_url() +
                         '/++resource++bika.lims.images/add.png'}
        self.show_sort_column = False
        self.show_select_row = False
        self.show_select_column = True
        self.pagesize = 50
        self.form_id = "arpriorities"

        self.icon = \
            self.portal_url + "/++resource++bika.lims.images/arpriority_big.png"
        self.title = self.context.translate(_("Analysis Request Priorities"))
        self.description = ""

        self.columns = {
            'title': {'title': _('Priority')},
            'sortKey': {'title': _('Sort Key')},
            'pricePremium': {'title': _('Premium')},
            'isDefault': {'title': _('Default')},
            'inactive_state': {'title': _('State')},
        }
        self.review_states = [
            {'id': 'default',
             'title': _('All'),
             'contentFilter': {},
             'columns': ['title',
                         'sortKey',
                         'pricePremium',
                         'isDefault',
                         'inactive_state']},
            {'id': 'draft',
             'title': _('Active'),
             'contentFilter': {'inactive_state': 'active'},
             'columns': ['title',
                         'sortKey',
                         'pricePremium',
                         'isDefault',
                         ]},
            {'id': 'inactive',
             'title': _('Inactive'),
             'contentFilter': {'inactive_state': 'inactive'},
             'columns': ['title',
                         'sortKey',
                         'pricePremium',
                         'isDefault',
                         ]},
        ]

    def folderitems(self):
        items = BikaListingView.folderitems(self)
        for x in range(len(items)):
            if 'obj' not in items[x]:
                continue

            items[x]['replace']['title'] = \
                "<a href='%s'>%s</a>" % (items[x]['url'], items[x]['title'])

        return items


schema = ATFolderSchema.copy()


class ARPriorities(ATFolder):
    implements(IARPriorities)
    displayContentsTab = False
    schema = schema

schemata.finalizeATCTSchema(schema, folderish=True, moveDiscussion=False)
atapi.registerType(ARPriorities, PROJECTNAME)
