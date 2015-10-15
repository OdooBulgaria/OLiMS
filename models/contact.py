"""The contact person at an organisation.
"""
# # ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import manage_users
# from dependencies.dependency import schemata
# from dependencies import atapi
# from dependencies.dependency import *
# from dependencies.dependency import permissions
# from dependencies.dependency import getToolByName
# from dependencies.dependency import safe_unicode
# from lims.config import ManageClients, PUBLICATION_PREFS, PROJECTNAME
# from lims.content.person import Person
# from lims import PMF, bikaMessageFactory as _
# from lims.interfaces import IContact
# from dependencies.dependency import implements
# from lims.utils import isActive

import logging

from openerp import fields, models

_logger = logging.getLogger(__name__)

from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.reference_field import ReferenceField
from fields.boolean_field import BooleanField

from fields.widget.widget import StringWidget, BooleanWidget
from dependencies.dependency import DisplayList
from dependencies.dependency import safe_unicode
from lims import PMF, bikaMessageFactory as _
from lims.utils import isActive

#schema = Person.schema.copy() + Schema((

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
    
    fields.Char(compute='computeFulname', string='fullname'),

      # ~~~~~~~ To be implemented ~~~~~~~
    # ComputedField('Fullname',
    #     expression = 'context.getFullname()',
    #     searchable = 1,
    #     widget = ComputedWidget(
    #         label=_("Full Name"),
    #         visible = {'edit': 'invisible', 'view': 'invisible'},
    #     ),
    # ),
    # StringField('Username',
    #     widget = StringWidget(
    #         visible = False
    #     ),
    # ),
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

        # note line filed multi-select , multi-select need to be implemented
            ReferenceField(string='PublicationPreference',
               selection=([ ('email', _('Email')), ('pdf', _('PDF'))]),
            # widget = MultiSelectionWidget(
            #     label=_("Publication preference"),
            # ),
    ),


    BooleanField('AttachmentsPermitted',
        default = False,
        schemata = 'Publication preference',
        widget = BooleanWidget(
            label=_("Results attachments permitted"),
            description = _(
                "File attachments to results, e.g. microscope "+ \
                "photos, will be included in emails to recipients "+ \
                "if this option is enabled")
        ),
    ),

    # ~~~~~~~ To be implemented ~~~~~~~
#     fields.Many2many(string='CCContact',
#                        comodel_name='olims.contact',
# #         schemata = 'Publication preference',
# #         vocabulary = 'getContacts',
# #         multiValued = 1,
# #         allowed_types = ('Contact',),
# #         relationship = 'ContactContact',
# #         widget = ReferenceWidget(
# #             checkbox_bound = 0,
# #             label=_("Contacts to CC"),
# #         ),
#         ),
 )

# schema['JobTitle'].schemata = 'default'
# schema['Department'].schemata = 'default'
# # Don't make title required - it will be computed from the Person's Fullname
# schema['title'].required = 0
# schema['title'].widget.visible = False
# schema.moveField('CCContact', before='AttachmentsPermitted')

class Contact(models.Model, BaseOLiMSModel): #(Person)
    _name = 'olims.contact'
    # implements(IContact)
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)
    
    def computeFulname(self):
        """ return Person's Fullname """
        for record in self:
        
            #record.Fullname_method = 'sdsdsdsdsd'
            fn = record.getFirstname()
            mi = record.getMiddleinitial()
            md = record.getMiddlename()
            sn = record.getSurname()
            fullname = ''
             
            if fn or sn:
                if mi and md:
                    fullname = '%s %s %s %s' % (record.getFirstname(),
                                            record.getMiddleinitial(),
                                            record.getMiddlename(),
                                            record.getSurname())
                elif mi:
                    fullname = '%s %s %s' % (record.getFirstname(),
                                            record.getMiddleinitial(),
                                            record.getSurname())
                elif md:
                    fullname = '%s %s %s' % (record.getFirstname(),
                                            record.getMiddlename(),
                                            record.getSurname())
                else:
                    fullname = '%s %s' % (record.getFirstname(), record.getSurname())
            record.fullname = fullname.strip()

        
    def Title(self):
        """ Return the contact's Fullname as title """
        return safe_unicode(self.getFullname()).encode('utf-8')

    #security.declareProtected(ManageClients, 'hasUser')
    def hasUser(self):
        """ check if contact has user """
        return self.portal_membership.getMemberById(
            self.getUsername()) is not None

    def getContacts(self, dl=True):
        pairs = []
        objects = []
        for contact in self.aq_parent.objectValues('Contact'):
            if isActive(contact) and contact.UID() != self.UID():
                pairs.append((contact.UID(), contact.Title()))
                if not dl:
                    objects.append(contact)
        pairs.sort(lambda x, y: cmp(x[1].lower(), y[1].lower()))
        return dl and DisplayList(pairs) or objects

    def getParentUID(self):
        return self.aq_parent.UID();

#atapi.registerType(Contact, PROJECTNAME)
Contact.initialze(schema)