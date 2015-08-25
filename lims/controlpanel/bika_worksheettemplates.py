from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import permissions
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims.browser import BrowserView
from OLiMS.lims.browser.bika_listing import BikaListingView
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.content.bikaschema import BikaFolderSchema
from OLiMS.dependencies.dependency import IViewView
from OLiMS.dependencies.dependency import ConflictError
from OLiMS.dependencies.dependency import IFolderContentsView
from OLiMS.dependencies.folder import ATFolder, ATFolderSchema
from OLiMS.lims.interfaces import IWorksheetTemplates
from OLiMS.dependencies.dependency import implements
import json

class WorksheetTemplatesView(BikaListingView):
    implements(IFolderContentsView, IViewView)

    def __init__(self, context, request):
        super(WorksheetTemplatesView, self).__init__(context, request)
        self.catalog = 'bika_setup_catalog'
        self.contentFilter = {'portal_type': 'WorksheetTemplate',
                              'sort_on': 'sortable_title'}
        self.context_actions = {_('Add'):
                                {'url': 'createObject?type_name=WorksheetTemplate',
                                 'icon': '++resource++bika.lims.images/add.png'}}
        self.title = self.context.translate(_("Worksheet Templates"))
        self.icon = self.portal_url + "/++resource++bika.lims.images/worksheettemplate_big.png"
        self.description = ""
        self.show_sort_column = False
        self.show_select_row = False
        self.show_select_column = True
        self.pagesize = 25

        self.columns = {
            'Title': {'title': _('Title'),
                      'index': 'sortable_title'},
            'Description': {'title': _('Description'),
                            'index': 'description',
                            'toggle': True},
            'Instrument': {'title': _('Instrument'),
                      'index':'getInstrumentTitle',
                      'toggle': True},
        }

        self.review_states = [
            {'id':'default',
             'title': _('Active'),
             'contentFilter': {'inactive_state': 'active'},
             'transitions': [{'id':'deactivate'}, ],
             'columns': ['Title',
                         'Description',
                         'Instrument']},
            {'id':'inactive',
             'title': _('Dormant'),
             'contentFilter': {'inactive_state': 'inactive'},
             'transitions': ['activate', ],
             'columns': ['Title',
                         'Description',
                         'Instrument']},
            {'id':'all',
             'title': _('All'),
             'contentFilter':{},
             'columns': ['Title',
                         'Description',
                         'Instrument']},
        ]

    def folderitems(self):
        items = BikaListingView.folderitems(self)
        for x in range(len(items)):
            if not items[x].has_key('obj'): continue
            obj = items[x]['obj']
            items[x]['Description'] = obj.Description()
            items[x]['Instrument'] = obj.getInstrument() and obj.getInstrument().Title() or ' '
            items[x]['replace']['Title'] = "<a href='%s'>%s</a>" % \
                 (items[x]['url'], items[x]['Title'])
        return items

schema = ATFolderSchema.copy()
class WorksheetTemplates(ATFolder):
    implements(IWorksheetTemplates)
    displayContentsTab = False
    schema = schema

schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)
atapi.registerType(WorksheetTemplates, PROJECTNAME)
