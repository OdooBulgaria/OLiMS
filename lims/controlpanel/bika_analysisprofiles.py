from lims.utils import isActive
from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import schemata
from dependencies import atapi
from dependencies.dependency import registerType
from dependencies.dependency import getToolByName
from lims.browser.bika_listing import BikaListingView
from lims.config import PROJECTNAME
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.content.bikaschema import BikaFolderSchema
from dependencies.dependency import IFolderContentsView
from dependencies.folder import ATFolder, ATFolderSchema
from dependencies.dependency import IViewView
from lims.interfaces import IAnalysisProfiles
from dependencies.dependency import implements

class ProfilesView(BikaListingView):

    def __init__(self, context, request):
        super(ProfilesView, self).__init__(context, request)
        self.catalog = "bika_setup_catalog"
        self.contentFilter = {
            'portal_type': 'AnalysisProfile',
            'sort_on': 'sortable_title',
            'path': {
                "query": "/".join(self.context.getPhysicalPath()),
                "level" : 0 },
        }
        self.show_sort_column = False
        self.show_select_row = False
        self.show_select_column = True
        self.icon = self.portal_url + "/++resource++bika.lims.images/analysisprofile_big.png"
        self.title = self.context.translate(_("Analysis Profiles"))
        self.context_actions = {_('Add Profile'):
                                {'url': 'createObject?type_name=AnalysisProfile',
                                 'icon': '++resource++bika.lims.images/add.png'}}

        self.columns = {
            'Title': {'title': _('Profile'),
                      'index': 'sortable_title'},
            'Description': {'title': _('Description'),
                            'index': 'Description'},
            'ProfileKey': {'title': _('Profile Key')},
        }

        self.review_states = [
            {'id':'default',
             'title': _('Active'),
             'contentFilter': {'inactive_state':'active'},
             'columns': ['Title',
                         'Description',
                         'ProfileKey']},
            {'id':'inactive',
             'title': _('Dormant'),
             'contentFilter': {'inactive_state':'inactive'},
             'columns': ['Title',
                         'Description',
                         'ProfileKey']},
            {'id':'all',
             'title': _('All'),
             'contentFilter':{},
             'columns': ['Title',
                         'Description',
                         'ProfileKey']},
        ]

    def folderitems(self):
        items = BikaListingView.folderitems(self)
        for x in range(len(items)):
            if not items[x].has_key('obj'): continue
            obj = items[x]['obj']
            items[x]['Title'] = obj.Title()
            items[x]['replace']['Title'] = "<a href='%s'>%s</a>" % \
                                           (items[x]['url'], items[x]['title'])
            items[x]['ProfileKey'] = obj.getProfileKey()
        return items

schema = ATFolderSchema.copy()
class AnalysisProfiles(ATFolder):
    implements(IAnalysisProfiles)
    displayContentsTab = False
    schema = schema

schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)
atapi.registerType(AnalysisProfiles, PROJECTNAME)
