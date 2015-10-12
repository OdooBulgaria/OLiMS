"""
    AnalysisRequests often use the same configurations.
    AnalysisProfile is used to save these common configurations (templates).
"""
import logging

from openerp import fields, models,osv

_logger = logging.getLogger(__name__)



from dependencies.dependency import ClassSecurityInfo
from lims import PMF, bikaMessageFactory as _

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from lims.browser.widgets import AnalysisProfileAnalysesWidget
# from lims.browser.widgets import ServicesWidget
# from lims.content.bikaschema import BikaSchema
# from lims.interfaces import IAnalysisProfile
# from dependencies.dependency import Interface, implements
# from dependencies.dependency import *
# from dependencies.dependency import RecordsField
# from lims.config import PROJECTNAME
# from dependencies.dependency import HoldingReference


from dependencies.dependency import getToolByName
from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.text_field import TextField
from fields.boolean_field import BooleanField
from fields.fixed_point_field import FixedPointField
from fields.widget.widget import StringWidget, AnalysisProfileAnalysesWidget, \
                                 TextAreaWidget, ComputedWidget, \
                                 BooleanWidget, DecimalWidget

# ~~~~~ Useful code that need to be converted in Odoo style ~~~~~~ 
# schema = BikaSchema.copy() + Schema(

schema = (StringField('name',
              required=1,        
    ),
    TextField('Description',
        widget = TextAreaWidget(
            label=_('Description'),
            description=_('Used in item listings and search results.'),
        ),
    ),                 
    StringField('ProfileKey',
        widget = StringWidget(
            label = _("Profile Keyword"),
            description = _("The profile's keyword is used to uniquely identify " + \
                          "it in import files. It has to be unique, and it may " + \
                          "not be the same as any Calculation Interim field ID."),
        ),
    ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ReferenceField('Service',
#         schemata = 'Analyses',
#         required = 1,
#         multiValued = 1,
#         allowed_types = ('AnalysisService',),
#         relationship = 'AnalysisProfileAnalysisService',
#         widget = AnalysisProfileAnalysesWidget(
#             label = _("Profile Analyses"),
#             description = _("The analyses included in this profile, grouped per category"),
#         )
#     ),
    TextField('Remarks',
        searchable = True,
        default_content_type = 'text/plain',
        allowable_content_types = ('text/plain', ),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            macro = "bika_widgets/remarks",
            label = _("Remarks"),
            append_only = True,
        ),
    ),
    # Custom settings for the assigned analysis services
    # https://jira.bikalabs.com/browse/LIMS-1324
    # Fields:
    #   - uid: Analysis Service UID
    #   - hidden: True/False. Hide/Display in results reports
    
# ~~~~~~~ To be implemented ~~~~~~~
    
#     RecordsField('AnalysisServicesSettings',
#          required=0,
#          subfields=('uid', 'hidden',),
#          widget=ComputedWidget(visible=False),
#     ),

    StringField('CommercialID',
        searchable=1,
        required=0,
        schemata='Accounting',
        widget=StringWidget(
            visible={'view': 'visible', 'edit': 'visible'},
            label=_('Commercial ID'),
            description=_("The profile's commercial ID for accounting purposes."),
        ),
    ),
    # When it's set, the system uses the analysis profile's price to quote and the system's VAT is overridden by the
    # the analysis profile's specific VAT
    BooleanField('UseAnalysisProfilePrice',
        default=False,
        schemata='Accounting',
        widget=BooleanWidget(
            label=_("Use Analysis Profile Price"),
            description=_("When it's set, the system uses the analysis profile's price to quote and the system's VAT is"
                          " overridden by the analysis profile's specific VAT"),
        )
    ),
    # The price will only be used if the checkbox "use analysis profiles' price" is set.
    # This price will be used to quote the analyses instead of analysis service's price.
    FixedPointField('AnalysisProfilePrice',
        schemata="Accounting",
        default='0.00',
        widget=DecimalWidget(
            label = _("Price (excluding VAT)"),
            visible={'view': 'visible', 'edit': 'visible'},
        ),
    ),
          FixedPointField('AnalysisProfileVAT',
        schemata="Accounting",
        default='0.00',
        widget=DecimalWidget(
            label = _("Price (excluding VAT)"),
            visible={'view': 'visible', 'edit': 'visible'},
        ),
    ),
          
   fields.Float(compute='computeVATAmount',string='VATAmount'),
    
          
    # When the checkbox "use analysis profiles' price" is set, the AnalysisProfilesVAT should override
    # the system's VAT

    # This VAT amount is computed using the AnalysisProfileVAT instead of systems VAT
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('VATAmount',
#         coumpute='getVATAmount',       
#         schemata="Accounting",
#         expression='context.getVATAmount()',
#         widget=ComputedWidget(
#             label = _("VAT"),
#             visible={'view': 'visible', 'edit': 'invisible'},
#             ),
#     ),
   
   fields.Float(compute='computeTotalPrice',string='TotalPrice'),
   
#     ComputedField('TotalPrice',
#           schemata="Accounting",
#           coumpute='getTotalPrice',
#           expression='context.getTotalPrice()',
#           widget=ComputedWidget(
#               label = _("Total price"),
#               visible={'edit': 'hidden', }
#           ),
#     ),
)
#)

# ~~~~~~~~~~  Irrelevant code for Odoo ~~~~~~~~~~~
# schema['title'].widget.visible = True
# schema['description'].widget.visible = True
# IdField = schema['id']

     
class AnalysisProfile(models.Model, BaseOLiMSModel):
    _name = "olims.analysis_profile"
    
# ~~~~~~~~~~  Irrelevant code for Odoo ~~~~~~~~~~~
#     security = ClassSecurityInfo()
#     schema = schema
#     displayContentsTab = False
#     implements(IAnalysisProfile)
    
    
    
    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)
        
    def getClientUID(self):
        return self.aq_parent.UID();

    def getAnalysisServiceSettings(self, uid):
        """ Returns a dictionary with the settings for the analysis
            service that match with the uid provided.
            If there are no settings for the analysis service and
            profile, returns a dictionary with the key 'uid'
        """
        sets = [s for s in self.getAnalysisServicesSettings() \
                if s.get('uid','') == uid]
        return sets[0] if sets else {'uid': uid}

    def isAnalysisServiceHidden(self, uid):
        """ Checks if the analysis service that match with the uid
            provided must be hidden in results.
            If no hidden assignment has been set for the analysis in
            this profile, returns the visibility set to the analysis
            itself.
            Raise a TypeError if the uid is empty or None
            Raise a ValueError if there is no hidden assignment in this
                profile or no analysis service found for this uid.
        """
        if not uid:
            raise TypeError('None type or empty uid')
        sets = self.getAnalysisServiceSettings(uid)
        if 'hidden' not in sets:
            uc = getToolByName(self, 'uid_catalog')
            serv = uc(UID=uid)
            if serv and len(serv) == 1:
                return serv[0].getObject().getRawHidden()
            else:
                raise ValueError('%s is not valid' % uid)
        return sets.get('hidden', False)
    
        
#     def getVATAmount(self):
#         """ Compute AnalysisProfileVATAmount
#         """
#         for reccord  in self:
#             price, vat = self.getAnalysisProfilePrice(), self.getAnalysisProfileVAT()
#             self.VATAmount = float(price) * float(vat) / 100
#             
    def computeVATAmount(self):
        """ Compute AnalysisProfileVATAmount
        """
        for record  in self:
            price, vat = record.getAnalysisProfileVAT(), record.getAnalysisProfilePrice(), 
            record.VATAmount =  float(vat) * float(price)  / 100
            

    def computeTotalPrice(self):
        """
        Computes the final price using the VATAmount and the subtotal price
        """
        for reccord  in self:
            price, vat = reccord.getAnalysisProfilePrice(), reccord.getVATAmount()
            reccord.TotalPrice =  float(price)+float(vat)
        
#     def getTotalPrice(self):
#         """
#         Computes the final price using the VATAmount and the subtotal price
#         """
#         for reccord  in self:
#             price, vat = reccord.getAnalysisProfilePrice(), reccord.getVATAmount()
#             reccord.TotalPrice =  4000
#     
# ~~~~~~~~~~  Irrelevant code for Odoo ~~~~~~~~~~~
# registerType(AnalysisProfile, PROJECTNAME)

AnalysisProfile.initialze(schema)
