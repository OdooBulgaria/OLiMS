# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import RecordWidget
# from dependencies.dependency import *
# from lims.config import PROJECTNAME
# from dependencies.dependency import permissions as CMFCorePermissions
# from lims.content.bikaschema import BikaSchema, BikaFolderSchema
# from dependencies.dependency import ATFolder
# from lims.browser.fields import AddressField
# from lims.browser.widgets import AddressWidget
# from dependencies.dependency import getToolByName


from dependencies.dependency import safe_unicode
from lims import bikaMessageFactory as _
from openerp import fields, models
from fields.string_field import StringField
from fields.widget.widget import StringWidget
from models.base_olims_model import BaseOLiMSModel

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema = BikaFolderSchema.copy() + BikaSchema.copy() + ManagedSchema(
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
          
    # # ~~~~~~~~~~ PhysicalAddress behavior in Odoo is as selection field ~~~~~~~~~~~
    fields.Many2one(comodel_name='olims.country',string='physical_country'),
    fields.Many2one(comodel_name='olims.state',string='physical_state', domain="[('Country', '=', physical_country)]"),
    fields.Many2one(comodel_name='olims.district',string='physical_district', domain="[('State', '=', physical_state)]"),
    fields.Char(string='physical_city'),
    fields.Char(string='physical_postalcode'),
    fields.Char(string='physical_address'),       
          
    # # ~~~~~~~~~~ PostalAddress behavior in Odoo is as selection field ~~~~~~~~~~~
    fields.Many2one(comodel_name='olims.country',string='postal_country'),
    fields.Many2one(comodel_name='olims.state',string='postal_state', domain="[('Country', '=', postal_country)]"),
    fields.Many2one(comodel_name='olims.district',string='postal_district', domain="[('State', '=', postal_state)]"),
    fields.Char(string='postal_city'),
    fields.Char(string='postal_postalcode'),
    fields.Char(string='postal_address'),      
          
    # # ~~~~~~~~~~ BillingAddress behavior in Odoo is as selection field ~~~~~~~~~~~
    fields.Many2one(comodel_name='olims.country',string='billing_country'),
    fields.Many2one(comodel_name='olims.state',string='billing_state', domain="[('Country', '=', billing_country)]"),
    fields.Many2one(comodel_name='olims.district',string='billing_district', domain="[('State', '=', billing_state)]"),
    fields.Char(string='billing_city'),
    fields.Char(string='billing_postalcode'),
    fields.Char(string='billing_address'),      

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
)

# IdField = schema['id']
# IdField.widget.visible = {'edit': 'visible', 'view': 'invisible'}
# # Don't make title required - it will be computed from the Organisation's
# # Name
# TitleField = schema['title']
# TitleField.required = 0
# TitleField.widget.visible = {'edit': 'hidden', 'view': 'invisible'}

class Organisation(models.Model, BaseOLiMSModel): #ATFolder
    _name ='olims.organisation'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema
    #
    # security.declareProtected(CMFCorePermissions.View, 'getSchema')
    def getSchema(self):
        return self.schema

    def Title(self):
        """ Return the Organisation's Name as its title """
        field = self.getField('Name')
        field = field and field.get(self) or ''
        return safe_unicode(field).encode('utf-8')

    def setTitle(self, value):
        return self.setName(value)

    def getPossibleAddresses(self):
        return ['PhysicalAddress', 'PostalAddress', 'BillingAddress']

    def getPrintAddress(self):
        address_lines = []
        use_address = None
        if self.getPostalAddress().has_key('city') \
        and self.getPostalAddress()['city']:
            use_address = self.getPostalAddress()
        elif self.getPhysicalAddress().has_key('city') \
        and self.getPhysicalAddress()['city']:
                use_address = self.getPhysicalAddress()
        elif self.getBillingAddress().has_key('city') \
        and self.getBillingAddress()['city']:
            use_address = self.getBillingAddress()
        if use_address:
            if use_address['address']:
                address_lines.append(use_address['address'])
            city_line = ''
            if use_address['city']:
                city_line += use_address['city'] + ' '
            if use_address['zip']:
                city_line += use_address['zip'] + ' '
            if city_line:
                address_lines.append(city_line)

            statecountry_line = ''
            if use_address['state']:
                statecountry_line += use_address['state'] + ', '
            if use_address['country']:
                statecountry_line += use_address['country']
            if statecountry_line:
                address_lines.append(statecountry_line)


        return address_lines

#registerType(Organisation, PROJECTNAME)
Organisation.initialze(schema)