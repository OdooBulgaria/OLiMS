"""Customised Collections for querying catalog
"""
from dependencies.dependency import ClassSecurityInfo
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.browser.widgets import QueryWidget
from lims.browser.fields import QueryField
from lims.config import PROJECTNAME
from lims.interfaces import IQuery
from dependencies.dependency import PloneMessageFactory as _p
from dependencies.dependency import Collection
from dependencies.dependency import CollectionSchema
from dependencies.dependency import ICollection
from dependencies.dependency import DisplayList
from dependencies.dependency import ATCT_TOOLNAME
from dependencies import atapi
from dependencies.dependency import IntDisplayList
from dependencies.dependency import schemata
from dependencies.dependency.permissions import ModifyPortalContent, View
from dependencies.dependency import getToolByName
from dependencies.dependency import implements
from dependencies.dependency import (BooleanField,
                                       BooleanWidget,
                                       IntegerField,
                                       LinesField,
                                       IntegerWidget,
                                       InAndOutWidget,
                                       StringField,
                                       StringWidget)

QuerySchema = CollectionSchema.copy() + atapi.Schema((
    QueryField(
        name='query',
        registry_prefix='bika.lims.bika_catalog_query',
        catalog_name='bika_catalog',
        widget=QueryWidget(
            label=_(u"Search terms"),
            description=_(u"Define the search terms for the items you want to "
                          u"list by choosing what to match on. "
                          u"The list of results will be dynamically updated."),
            registry_prefix='bika.lims.bika_catalog_query',
            catalog_name='bika_catalog',
        ),
        validators=('javascriptDisabled', )
    ),

    StringField(
        name='sort_on',
        required=False,
        mode='rw',
        default='sortable_title',
        widget=StringWidget(
            label=_(u'Sort the collection on this index'),
            description='',
            visible=False,
        ),
    ),

    BooleanField(
        name='sort_reversed',
        required=False,
        mode='rw',
        default=False,
        widget=BooleanWidget(
            label=_(u'Sort the results in reversed order'),
            description='',
            visible=False,
        ),
    ),

    IntegerField(
        name='limit',
        required=False,
        mode='rw',
        default=1000,
        widget=IntegerWidget(
            label=_(u'Limit Search Results'),
            description=_(u"Specify the maximum number of items to show.")
        ),
    ),

    LinesField('customViewFields',
               required=False,
               mode='rw',
               default=('Title', 'Creator', 'Type', 'ModificationDate'),
               vocabulary='listMetaDataFields',
               enforceVocabulary=True,
               write_permission=ModifyPortalContent,
               widget=InAndOutWidget(
                   label=_(u'Table Columns'),
                   description=_(
                       u"Select which fields to display when "
                       u"'Tabular view' is selected in the display menu.")
               ),
               ),
))


class Query(Collection):

    """ Query form and results for bika_catalog objects/indexes
    """

    implements(ICollection, IQuery)
    meta_type = "Query"
    schema = QuerySchema
    security = ClassSecurityInfo()

    security.declareProtected(View, 'listMetaDataFields')

    def listMetaDataFields(self, exclude=True):
        """Return a list of metadata fields from catalog.
        """
        #tool = getToolByName(self, ATCT_TOOLNAME)
        #original_list = tool.getMetadataDisplay(exclude)

        return DisplayList((
            ('getAnalysisCategory', _p('Analysis Category')),
            ('getAnalysisService', _p('Analysis Service')),
            ('getAnalysts', _('Analyst')),
            ('getClientOrderNumber', _('Client Order')),
            ('getClientReference', _('Client Reference')),
            ('getClientSampleID', _('Client Sample ID')),
            ('getClientTitle', _('Client')),
            ('getContactTitle', _('Contact')),
            ('Creator', _p('Creator')),
            ('created', _('Date Created')),
            ('getDatePublished', _('Date Published')),
            ('getDateReceived', _('Date Received')),
            ('getDateSampled', _('Date Sampled')),
            ('getProfilesTitle', _('Analysis Profiles')),
            ('getRequestID', _('Request ID')),
            ('getSampleID', _('Sample ID')),
            ('getSamplePointTitle', _('Sample Point')),
            ('getSampleTypeTitle', _('Sample Type')),
            ('review_state', _p('Review state')),
        ))

    security.declareProtected(View, 'results')

    def results(self, batch=True, b_start=0, b_size=None, sort_on=None,
                brains=False, catalog_name='bika_catalog'):
        """Get results"""

        if sort_on is None:
            sort_on = self.getSort_on()
        if b_size is None:
            b_size = self.getLimit()

        return self.getQuery(batch=batch,
                             b_start=b_start,
                             b_size=b_size,
                             sort_on=sort_on,
                             brains=brains,
                             catalog_name='bika_catalog')

schemata.finalizeATCTSchema(QuerySchema, folderish=False)

atapi.registerType(Query, PROJECTNAME)
