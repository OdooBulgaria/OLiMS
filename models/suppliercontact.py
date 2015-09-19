"""The contact person at a reference supplier organisation.
"""
# # ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import manage_users
# from dependencies.dependency import *
# from lims.content.person import Person
# from dependencies.dependency import permissions
# from dependencies.dependency import getToolByName
# from lims.config import PROJECTNAME
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from dependencies.dependency import implements

from openerp import fields, models
from fields.string_field import StringField
from models.base_olims_model import BaseOLiMSModel
from fields.widget.widget import StringWidget
from lims import bikaMessageFactory as _
#schema = Person.schema.copy()

schema = (
     StringField('Salutation',
        widget = StringWidget(
            label = _("Salutation",
                      "Title"),
            description=_("Greeting title eg. Mr, Mrs, Dr"),
        ),
    ),
    StringField('Firstname',
        required = 1,
        widget = StringWidget(
            label=_("Firstname"),
        ),
    ),
    StringField('Middleinitial',
        required = 0,
        widget = StringWidget(
            label=_("Middle initial"),
        ),
    ),
    StringField('Middlename',
        required = 0,
        widget = StringWidget(
            label=_("Middle name"),
        ),
    ),
    StringField('Surname',
        required = 1,
        widget = StringWidget(
            label=_("Surname"),
        ),
    ),
    # ComputedField('Fullname',
    #     expression = 'context.getFullname()',
    #     searchable = 1,
    #     widget = ComputedWidget(
    #         label=_("Full Name"),
    #         visible = {'edit': 'invisible', 'view': 'invisible'},
    #     ),
    # ),
    StringField('Username',
        widget = StringWidget(
            visible = False
        ),
    ),
    StringField('EmailAddress',
        schemata = 'Email Telephone Fax',
        searchable = 1,
        widget = StringWidget(
            label=_("Email Address"),
        ),
    ),
    StringField('BusinessPhone',
        schemata = 'Email Telephone Fax',
        widget = StringWidget(
            label=_("Phone (business)"),
        ),
    ),
    StringField('BusinessFax',
        schemata = 'Email Telephone Fax',
        widget = StringWidget(
            label=_("Fax (business)"),
        ),
    ),
    StringField('HomePhone',
        schemata = 'Email Telephone Fax',
        widget = StringWidget(
            label=_("Phone (home)"),
        ),
    ),
    StringField('MobilePhone',
        schemata = 'Email Telephone Fax',
        widget = StringWidget(
            label=_("Phone (mobile)"),
        ),
    ),
    StringField('JobTitle',
        widget = StringWidget(
            label=_("Job title"),
        ),
    ),
    StringField('Department',
        widget = StringWidget(
            label=_("Department"),
        ),
    ),
    # AddressField('PhysicalAddress',
    #     schemata = 'Address',
    #     widget = AddressWidget(
    #        label=_("Physical address"),
    #     ),
    # ),
    # AddressField('PostalAddress',
    #     schemata = 'Address',
    #     widget = AddressWidget(
    #        label=_("Postal address"),
    #     ),
    # ),

)

# schema['JobTitle'].schemata = 'default'
# schema['Department'].schemata = 'default'
#
# schema['id'].schemata = 'default'
# schema['id'].widget.visible = False
# # Don't make title required - it will be computed from the Person's
# # Fullname
# schema['title'].schemata = 'default'
# schema['title'].required = 0
# schema['title'].widget.visible = False

class SupplierContact(models.Model, BaseOLiMSModel): #Person
    _name = 'olims.supplier_contact'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

#registerType(SupplierContact, PROJECTNAME)

SupplierContact.initialze(schema)