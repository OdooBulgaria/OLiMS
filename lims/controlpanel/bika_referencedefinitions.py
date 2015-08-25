from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import registerType
from OLiMS.dependencies.dependency import permissions
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.lims.browser import BrowserView
from OLiMS.lims.browser.bika_listing import BikaListingView
from OLiMS.lims.config import PROJECTNAME
from OLiMS.dependencies.dependency import IViewView
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.content.bikaschema import BikaFolderSchema
from OLiMS.dependencies.dependency import IFolderContentsView
from OLiMS.dependencies.folder import ATFolder, ATFolderSchema
from OLiMS.lims.interfaces import IReferenceDefinitions
from OLiMS.dependencies.dependency import implements

class ReferenceDefinitionsView(BikaListingView):
    implements(IFolderContentsView, IViewView)
    def __init__(self, context, request):
        super(ReferenceDefinitionsView, self).__init__(context, request)
        self.catalog = 'bika_setup_catalog'
        self.contentFilter = {'portal_type': 'ReferenceDefinition',
                              'sort_on': 'sortable_title'}
        self.context_actions = {_('Add'):
                                {'url': 'createObject?type_name=ReferenceDefinition',
                                 'icon': '++resource++bika.lims.images/add.png'}}
        self.icon = self.portal_url + "/++resource++bika.lims.images/referencedefinition_big.png"
        self.title = self.context.translate(_("Reference Definitions"))
        self.description = self.context.translate(_(
            "ReferenceDefinition represents a Reference Definition "
            "or sample type used for quality control testing"))
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
        }

        self.review_states = [
            {'id':'default',
             'title': _('Active'),
             'contentFilter': {'inactive_state': 'active'},
             'transitions': [{'id':'deactivate'}, ],
             'columns': ['Title', 'Description']},
            {'id':'inactive',
             'title': _('Dormant'),
             'contentFilter': {'inactive_state': 'inactive'},
             'transitions': [{'id':'activate'}, ],
             'columns': ['Title', 'Description']},
            {'id':'all',
             'title': _('All'),
             'contentFilter':{},
             'columns': ['Title', 'Description']},
        ]

    def folderitems(self):
        items = BikaListingView.folderitems(self)
        for x in range(len(items)):
            if not items[x].has_key('obj'): continue
            obj = items[x]['obj']
            items[x]['Description'] = obj.Description()
            items[x]['replace']['Title'] = "<a href='%s'>%s</a>" % \
                 (items[x]['url'], items[x]['Title'])

            after_icons = ''
            if obj.getBlank():
                after_icons += "<img src='++resource++bika.lims.images/blank.png' title='Blank'>"
            if obj.getHazardous():
                after_icons += "<img src='++resource++bika.lims.images/hazardous.png' title='Hazardous'>"
            items[x]['replace']['Title'] = "<a href='%s'>%s</a>&nbsp;%s" % \
                 (items[x]['url'], items[x]['Title'], after_icons)

        return items

schema = ATFolderSchema.copy()
class ReferenceDefinitions(ATFolder):
    implements(IReferenceDefinitions)
    displayContentsTab = False
    schema = schema

schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)
atapi.registerType(ReferenceDefinitions, PROJECTNAME)
