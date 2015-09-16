"""Client - the main organisational entity in bika.
"""


# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import schemata
# from dependencies import atapi
# from dependencies.dependency import permissions
# from lims import interfaces
# from lims.config import *
# from lims.content.organisation import Organisation
# from lims.interfaces import IClient
# from lims.utils import isActive
# from dependencies.dependency import getUtility
# from dependencies.dependency import implements
# from dependencies.dependency import alsoProvides



import logging

from openerp import fields, models,osv

_logger = logging.getLogger(__name__)

from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.reference_field import ReferenceField
from fields.boolean_field import BooleanField
from fields.text_field import TextField
from fields.widget.widget import  TextAreaWidget, ReferenceWidget, StringWidget, BooleanWidget
from lims import bikaMessageFactory as _
from dependencies.dependency import DisplayList
from dependencies.dependency import getToolByName
from dependencies.dependency import safe_unicode
from lims import PMF, bikaMessageFactory as _
from lims.workflow import getCurrentState, StateFlow, InactiveState

import json
import sys

#schema = Organisation.schema.copy() + atapi.Schema((

schema = (

    StringField('Name',
        required = 1,
        searchable = True,
        validators = ('uniquefieldvalidator',),
        widget = StringWidget(
            label=_("Name"),
        ),
    ),
    StringField('TaxNumber',
        widget = StringWidget(
            label=_("VAT number"),
        ),
    ),
    StringField('Phone',
        widget = StringWidget(
            label=_("Phone"),
        ),
    ),
    StringField('Fax',
        widget = StringWidget(
            label=_("Fax"),
        ),
    ),
    StringField('EmailAddress',
        schemata = 'Address',
        widget = StringWidget(
            label=_("Email Address"),
        ),
        validators = ('isEmail',)
    ),
# # ~~~~~~~~~~ AddressField behavior in Odoo is as selection field ~~~~~~~~~~~
#     AddressField('PhysicalAddress',
#         schemata = 'Address',
#         widget = AddressWidget(
#            label=_("Physical address"),
#         ),
#     ),
#     AddressField('PostalAddress',
#         schemata = 'Address',
#         widget = AddressWidget(
#            label=_("Postal address"),
#         ),
#     ),
#     AddressField('BillingAddress',
#         schemata = 'Address',
#         widget = AddressWidget(
#            label=_("Billing address"),
#         ),
#    ),
    StringField('AccountType',
        schemata = 'Bank details',
        widget = StringWidget(
            label=_("Account Type"),
        ),
    ),
    StringField('AccountName',
        schemata = 'Bank details',
        widget = StringWidget(
            label=_("Account Name"),
        ),
    ),
    StringField('AccountNumber',
        schemata = 'Bank details',
        widget = StringWidget(
            label=_("Account Number"),
        ),
    ),
    StringField('BankName',
        schemata = 'Bank details',
        widget = StringWidget(
            label=_("Bank name"),
        ),
    ),
    StringField('BankBranch',
        schemata = 'Bank details',
        widget = StringWidget(
            label=_("Bank branch"),
        ),
    ),


    StringField('ClientID',
        required=1,
        searchable = True,
        #validators = ('uniquefieldvalidator', 'standard_id_validator'),
        widget=StringWidget(
            label=_('Client ID'),
            description=_('Title is required.'),
        ),
    ),

    BooleanField('BulkDiscount',
        default = False,
        #write_permission = ManageClients,
        widget = BooleanWidget(
            label=_("Bulk discount applies"),
        ),
    ),

    BooleanField('MemberDiscountApplies',
        default = False,
        #write_permission = ManageClients,
        widget = BooleanWidget(
            label=_("Member discount applies"),
        ),
    ),

    # ~~~~~~~ To be implemented ~~~~~~~
    # atapi.LinesField('EmailSubject',
    #     schemata = 'Preferences',
    #     default = ['ar', ],
    #     vocabulary = EMAIL_SUBJECT_OPTIONS,
    #     widget = atapi.MultiSelectionWidget(
    #         description=_("Items to be included in email subject lines"),
    #         label=_("Email subject line"),
    #     ),
    # ),


    ReferenceField(string='DefaultCategories',
           selection=[('olims.analysis_category', 'AnalysisCategory')],
           required=0,
            widget = ReferenceWidget(
            checkbox_bound = 0,
            #label=_("Default categories"),
            help=_("Always expand the selected categories in client views"),
        ),
    ),
    ## ~~~~~~~ To be implemented ~~~~~~~ multiValued
    # atapi.ReferenceField('DefaultCategories',
    #     schemata = 'Preferences',
    #     required = 0,
    #     multiValued = 1,
    #     vocabulary = 'getAnalysisCategories',
    #     vocabulary_display_path_bound = sys.maxint,
    #     allowed_types = ('AnalysisCategory',),
    #     relationship = 'ClientDefaultCategories',
    #     widget = atapi.ReferenceWidget(
    #         checkbox_bound = 0,
    #         label=_("Default categories"),
    #         description=_("Always expand the selected categories in client views"),
    #     ),
    # ),

    ReferenceField(string='RestrictedCategories',
               selection=[('olims.analysis_category', 'AnalysisCategory')],
               required=0,
                widget = ReferenceWidget(
                checkbox_bound = 0,
                #label=_("Default categories"),
                help=_("Always expand the selected categories in client views"),
            ),
        ),
    ## ~~~~~~~ To be implemented ~~~~~~~ multiValued
    # atapi.ReferenceField('RestrictedCategories',
    #     schemata = 'Preferences',
    #     required = 0,
    #     multiValued = 1,
    #     vocabulary = 'getAnalysisCategories',
    #     validators = ('restrictedcategoriesvalidator',),
    #     vocabulary_display_path_bound = sys.maxint,
    #     allowed_types = ('AnalysisCategory',),
    #     relationship = 'ClientRestrictedCategories',
    #     widget = atapi.ReferenceWidget(
    #         checkbox_bound = 0,
    #         label=_("Restrict categories"),
    #         description=_("Show only selected categories in client views"),
    #     ),
    # ),



    fields.Selection(string='DefaultARSpecs',
         selection=( ('ar_specs', 'Analysis Request Specifications'),
                                 ('lab_sampletype_specs', 'Sample Type Specifications (Lab)'),
                                 ('client_sampletype_specs', 'Sample Type Specifications (Client)')),
         help="DefaultARSpecs_description",
    #     schemata = "Preferences",
         default = 'ar_specs',
    #     vocabulary =  DEFAULT_AR_SPECS,
    #     widget = atapi.SelectionWidget(
    #         label=_("Default AR Specifications"),
    #         description=_("DefaultARSpecs_description"),
    #         format='select',
    #     )
     ),

    BooleanField('DefaultDecimalMark',
        default = True,
        #write_permission = ManageClients,
         widget = BooleanWidget(
            label=_("Default decimal mark"),
            description=_("The decimal mark selected in Bika Setup will be used."),
        ),
    ),



    fields.Selection(string='DecimalMark',
         selection=(
                    ('.', _('Dot (.)')),
                    (',', _('Comma (,)')),
                                    ),
         help="Decimal mark to use in the reports from this Client.",
    #     schemata = "Preferences",
         default = '.',
    #     vocabulary =  DECIMAL_MARKS,
    #     widget = atapi.SelectionWidget(
    #         label=_("Custom decimal mark"),
    #         description=_("Decimal mark to use in the reports from this Client."),
    #         format = 'select',
    #     )
     ),

)

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['AccountNumber'].write_permission = ManageClients
# schema['title'].widget.visible = False
# schema['description'].widget.visible = False
# schema['EmailAddress'].schemata = 'default'
#
# schema.moveField('ClientID', after='Name')

class Client(models.Model, BaseOLiMSModel):#(Organisation):
    _name='olims.client'
    # implements(IClient)
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def Title(self):
        """ Return the Organisation's Name as its title """
        return safe_unicode(self.getField('Name').get(self)).encode('utf-8')

    #security.declarePublic('getContactFromUsername')
    def getContactFromUsername(self, username):
        for contact in self.objectValues('Contact'):
            if contact.getUsername() == username:
                return contact.UID()

    #security.declarePublic('getContactUIDForUser')
    def getContactUIDForUser(self):
        """ get the UID of the user associated with the authenticated user
        """
        membership_tool = getToolByName(self, 'portal_membership')
        member = membership_tool.getAuthenticatedMember()
        username = member.getUserName()
        r = self.portal_catalog(
            portal_type = 'Contact',
            getUsername = username
        )
        if len(r) == 1:
            return r[0].UID


    #security.declarePublic('getARImportOptions')
    def getARImportOptions(self):
        return ARIMPORT_OPTIONS

    #security.declarePublic('getAnalysisCategories')
    def getAnalysisCategories(self):
        """ return all available analysis categories """
        bsc = getToolByName(self, 'bika_setup_catalog')
        cats = []
        for st in bsc(portal_type = 'AnalysisCategory',
                      inactive_state = 'active',
                      sort_on = 'sortable_title'):
            cats.append((st.UID, st.Title))
        return DisplayList(cats)

    def getContacts(self, only_active=True):
        """ Return an array containing the contacts from this Client
        """
        contacts = []
        if only_active:
            contacts = [c for c in self.objectValues('Contact') if
                        getCurrentState(c, StateFlow.inactive) == InactiveState.active]
        else:
            contacts = self.objectValues('Contact')
        return contacts;

    def getDecimalMark(self):
        """ Return the decimal mark to be used on reports for this
            client. If the client has DefaultDecimalMark selected, the
            Default value from Bika Setup will be returned. Otherwise,
            will return the value of DecimalMark.
        """
        if self.getDefaultDecimalMark() == False:
            return self.Schema()['DecimalMark'].get(self)
        return self.bika_setup.getDecimalMark()


# schemata.finalizeATCTSchema(schema, folderish = True, moveDiscussion = False)
#
# atapi.registerType(Client, PROJECTNAME)

Client.initialze(schema)
