# # ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from lims.config import PROJECTNAME, ManageSuppliers
# from lims.content.bikaschema import BikaSchema
# from lims.content.organisation import Organisation
# from lims.interfaces import ISupplier
# from dependencies.dependency import *
# from dependencies.dependency import safe_unicode
# from dependencies.dependency import implements
#schema = Organisation.schema.copy() + ManagedSchema((


from dependencies.dependency import safe_unicode
from lims import bikaMessageFactory as _
from openerp import fields, models
from fields.string_field import StringField
from fields.text_field import TextField
from fields.widget.widget import TextAreaWidget, StringWidget
from models.base_olims_model import BaseOLiMSModel



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
# ~~~~~~~~~~ AddressField behavior in Odoo is as selection field ~~~~~~~~~~~
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
#     ),
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


    TextField('Remarks',
        searchable = True,
        default_content_type = 'text/plain',
        allowed_content_types= ('text/plain', ),
        default_output_type = "text/html",
        widget = TextAreaWidget(
            macro = "bika_widgets/remarks",
            label=_("Remarks"),
            append_only = True,
        ),
    ),
    StringField('Website',
        searchable=1,
        required=0,
        widget=StringWidget(
            visible={'view': 'visible', 'edit': 'visible'},
            label=_('Website.'),
        ),
    ),
    StringField('NIB',
        searchable=1,
        schemata = 'Bank details',
        required=0,
        widget=StringWidget(
            visible={'view': 'visible', 'edit': 'visible'},
            label=_('NIB'),
        ),
        validators=('NIBvalidator'),
    ),
    StringField('IBN',
        searchable=1,
        schemata ='Bank details',
        required=0,
        widget=StringWidget(
            visible={'view': 'visible', 'edit': 'visible'},
            label=_('IBN'),
        ),
        validators=('IBANvalidator'),
    ),
    StringField('SWIFTcode',
        searchable=1,
        required=0,
        schemata ='Bank details',
        widget=StringWidget(
            visible={'view': 'visible', 'edit': 'visible'},
            label=_('SWIFT code.'),
        ),
    ),
)

#schema['AccountNumber'].write_permission = ManageSuppliers

class Supplier(models.Model, BaseOLiMSModel): #Organisation
    _name='olims.supplier'
    # implements(ISupplier)
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    def Title(self):
        """ Return the Organisation's Name as its title """
        return safe_unicode(self.getField('Name').get(self)).encode('utf-8')

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

#registerType(Supplier, PROJECTNAME)
Supplier.initialze(schema)