from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import schemata
from dependencies import atapi
from dependencies.dependency import permissions
from dependencies.dependency import getToolByName
from lims.browser.bika_listing import BikaListingView
from lims.config import PROJECTNAME
from lims import bikaMessageFactory as _
from lims.utils import t
from dependencies.dependency import IFolderContentsView
from dependencies.folder import ATFolder, ATFolderSchema
from lims.interfaces import IAnalysisSpecs
from dependencies.dependency import implements
from dependencies.dependency import IViewView

class AnalysisSpecsView(BikaListingView):
    implements(IFolderContentsView, IViewView)

    def __init__(self, context, request):
        super(AnalysisSpecsView, self).__init__(context, request)
        self.catalog = 'bika_setup_catalog'
        self.contentFilter = {'portal_type': 'AnalysisSpec',
                              'sort_on': 'sortable_title',
                              'path': {'query':"/".join(self.context.getPhysicalPath()),
                                       'level':0}}
        self.context_actions = {_('Add'):
                                {'url': 'createObject?type_name=AnalysisSpec',
                                 'icon': '++resource++bika.lims.images/add.png'}}
        self.icon = self.portal_url + "/++resource++bika.lims.images/analysisspec_big.png"
        self.title = self.context.translate(_("Analysis Specifications"))
        self.description = self.context.translate(_(
            "Set up the laboratory analysis service results specifications"))
        self.show_sort_column = False
        self.show_select_row = False
        self.show_select_column = True
        self.pagesize = 25

        self.columns = {
            'Title': {'title': _('Title'),
                           'index': 'title'},
            'SampleType': {'title': _('Sample Type'),
                           'index': 'sortable_title'},
        }

        self.review_states = [
            {'id':'default',
             'title': _('Active'),
             'contentFilter': {'inactive_state': 'active'},
             'transitions': [{'id':'deactivate'}, ],
             'columns': ['Title', 'SampleType']},
            {'id':'inactive',
             'title': _('Dormant'),
             'contentFilter': {'inactive_state': 'inactive'},
             'transitions': [{'id':'activate'}, ],
             'columns': ['Title', 'SampleType']},
            {'id':'all',
             'title': _('All'),
             'contentFilter':{},
             'columns': ['Title', 'SampleType']},
        ]

    def folderitems(self):
        items = BikaListingView.folderitems(self)
        for x in range(len(items)):
            if not items[x].has_key('obj'): continue
            obj = items[x]['obj']
            items[x]['Title'] = obj.Title()
            items[x]['replace']['Title'] = "<a href='%s'>%s</a>" % \
                 (items[x]['url'], items[x]['Title'])
            st = obj.getSampleType()
            items[x]['SampleType'] = obj.getSampleType().Title() \
                if obj.getSampleType() else ""
        return items

schema = ATFolderSchema.copy()
class AnalysisSpecs(ATFolder):
    implements(IAnalysisSpecs)
    displayContentsTab = False
    schema = schema

schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)
atapi.registerType(AnalysisSpecs, PROJECTNAME)
