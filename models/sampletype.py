# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import HistoryAwareMixin
# from dependencies.dependency import *
# from dependencies.dependency import HoldingReference
# from lims.browser import BrowserView
# from lims.config import PROJECTNAME
# from lims.browser.widgets import DurationWidget
# from lims.browser.fields import DurationField
# from lims.content.bikaschema import BikaSchema
# from lims.interfaces import ISampleType
# from magnitude import mg, MagnitudeError
# from dependencies.dependency import implements
# import json
import sys
from dependencies.dependency import getToolByName
from dependencies.dependency import safe_unicode
from lims import bikaMessageFactory as _
from openerp import fields, models
from fields.string_field import StringField
from fields.text_field import TextField
from fields.boolean_field import BooleanField
from fields.widget.widget import TextAreaWidget, BooleanWidget, StringWidget
from models.base_olims_model import BaseOLiMSModel
from lims.utils import t
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema = BikaSchema.copy() + Schema((
schema = (StringField('name',
              required=1,        
    ),
    TextField('Description',
              widget=TextAreaWidget(
                label=_('Description'),
                description=_('Used in item listings and search results.')),    
    ),
          
    fields.Char(string='Days', required=True),
    fields.Char(string='Hours', required=True),
    fields.Char(string='Minutes', required=True),    
      
# ~~~~~~~ To be implemented ~~~~~~~
#     DurationField('RetentionPeriod',
#         required = 1,
#         default_method = 'getDefaultLifetime',
#         widget = DurationWidget(
#             label=_("Retention Period"),
#             description =_(
#                 "The period for which un-preserved samples of this type can be kept before "
#                 "they expire and cannot be analysed any further"),
#         )
#     ),
    BooleanField('Hazardous',
        default = False,
        widget = BooleanWidget(
            label=_("Hazardous"),
            description=_("Samples of this type should be treated as hazardous"),
        ),
    ),
    fields.Many2one(string='SampleMatrix',
                    comodel_name='olims.sample_matrix',
        required = False,
#         allowed_types = ('SampleMatrix',),
#         vocabulary = 'SampleMatricesVocabulary',
#         relationship = 'SampleTypeSampleMatrix',
#         referenceClass = HoldingReference,
#         widget = ReferenceWidget(
#             checkbox_bound = 0,
#             label=_("Sample Matrix"),
#         ),
    ),
    StringField('Prefix',
        required = True,
        widget = StringWidget(
            label=_("Sample Type Prefix"),
        ),
    ),
    StringField('MinimumVolume',
        required = 1,
        widget = StringWidget(
            label=_("Minimum Volume"),
            description=_("The minimum sample volume required for analysis eg. '10 ml' or '1 kg'."),
        ),
    ),
    fields.Many2one(string='ContainerType',
        comodel_name='olims.container_type',
        required = False,
        help="The default container type. New sample partitions " + \
                "are automatically assigned a container of this " + \
                "type, unless it has been specified in more details " + \
                "per analysis service",
#         allowed_types = ('ContainerType',),
#         vocabulary = 'ContainerTypesVocabulary',
#         relationship = 'SampleTypeContainerType',
#         widget = ReferenceWidget(
#             checkbox_bound = 0,
#             label=_("Default Container Type"),
#             description =_(
#                 "The default container type. New sample partitions "
#                 "are automatically assigned a container of this "
#                 "type, unless it has been specified in more details "
#                 "per analysis service"),
#         ),
    ),

    fields.Many2many(string='SamplePoints',
        required = False,
        comodel_name = 'olims.sample_point',
        help="The list of sample points from which this sample " + \
                            "type can be collected.  If no sample points are " + \
                            "selected, then all sample points are available."
#         multiValued = 1,
#         allowed_types = ('SamplePoint',),
#         vocabulary = 'SamplePointsVocabulary',
#         relationship = 'SampleTypeSamplePoint',
#         widget = ReferenceWidget(
#             checkbox_bound = 0,
#             label=_("Sample Points"),
#             description =_("The list of sample points from which this sample "
#                            "type can be collected.  If no sample points are "
#                            "selected, then all sample points are available."),
#         ),
    ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField(
#         'SamplePointTitle',
#         expression="[o.Title() for o in context.getSamplePoints()]",
#         widget = ComputedWidget(
#             visibile=False,
#         )
#     ),
)#)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['description'].schemata = 'default'
# schema['description'].widget.visible = True

class SampleType(models.Model, BaseOLiMSModel):#(BaseContent, HistoryAwareMixin):
    _name = 'olims.sample_type'
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#     implements(ISampleType)
#     security = ClassSecurityInfo()
#     displayContentsTab = False
#     schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def Title(self):
        return safe_unicode(self.getField('title').get(self)).encode('utf-8')
# ~~~~~~~ To be implemented ~~~~~~~
#     def getJSMinimumVolume(self, **kw):
#         """Try convert the MinimumVolume to 'ml' or 'g' so that JS has an
#         easier time working with it.  If conversion fails, return raw value.
#         """
#         default = self.Schema()['MinimumVolume'].get(self)
#         try:
#             mgdefault = default.split(' ', 1)
#             mgdefault = mg(float(mgdefault[0]), mgdefault[1])
#         except:
#             mgdefault = mg(0, 'ml')
#         try:
#             return str(mgdefault.ounit('ml'))
#         except:
#             pass
#         try:
#             return str(mgdefault.ounit('g'))
#         except:
#             pass
#         return str(default)

    def getDefaultLifetime(self):
        """ get the default retention period """
        settings = getToolByName(self, 'bika_setup')
        return settings.getDefaultSampleLifetime()

    def SamplePointsVocabulary(self):
        from lims.content.samplepoint import SamplePoints
        return SamplePoints(self, allow_blank=False)

    def setSamplePoints(self, value, **kw):
        """ For the moment, we're manually trimming the sampletype<>samplepoint
            relation to be equal on both sides, here.
            It's done strangely, because it may be required to behave strangely.
        """
        bsc = getToolByName(self, 'bika_setup_catalog')
        ## convert value to objects
        if value and type(value) == str:
            value = [bsc(UID=value)[0].getObject(),]
        elif value and type(value) in (list, tuple) and type(value[0]) == str:
            value = [bsc(UID=uid)[0].getObject() for uid in value if uid]
        ## Find all SamplePoints that were removed
        existing = self.Schema()['SamplePoints'].get(self)
        removed = existing and [s for s in existing if s not in value] or []
        added = value and [s for s in value if s not in existing] or []
        ret = self.Schema()['SamplePoints'].set(self, value)

        for sp in removed:
            sampletypes = sp.getSampleTypes()
            if self in sampletypes:
                sampletypes.remove(self)
                sp.setSampleTypes(sampletypes)

        for sp in added:
            sp.setSampleTypes(list(sp.getSampleTypes()) + [self,])

        return ret

    def getSamplePoints(self, **kw):
        return self.Schema()['SamplePoints'].get(self)

    def SampleMatricesVocabulary(self):
        from lims.content.samplematrix import SampleMatrices
        return SampleMatrices(self, allow_blank=True)

    def ContainerTypesVocabulary(self):
        from lims.content.containertype import ContainerTypes
        return ContainerTypes(self, allow_blank=True)
SampleType.initialze(schema)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# registerType(SampleType, PROJECTNAME)
# ~~~~~~~ To be implemented ~~~~~~~
# def SampleTypes(self, instance=None, allow_blank=False):
#     instance = instance or self
#     bsc = getToolByName(instance, 'bika_setup_catalog')
#     items = []
#     for st in bsc(portal_type='SampleType',
#                   inactive_state='active',
#                   sort_on = 'sortable_title'):
#         items.append((st.UID, st.Title))
#     items = allow_blank and [['','']] + list(items) or list(items)
#     return DisplayList(items)
