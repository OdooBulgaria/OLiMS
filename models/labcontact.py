"""The lab staff
"""
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import manage_users
# from dependencies.dependency import permissions
# from dependencies.dependency import getToolByName
# from dependencies.dependency import safe_unicode
# from dependencies.dependency import *
# from dependencies.dependency import HoldingReference
# from lims.content.person import Person
# from lims.config import PUBLICATION_PREFS, PROJECTNAME
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from dependencies.dependency import implements
# from lims.interfaces import ILabContact
# import sys

from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.file_field import FileField
from fields.widget.widget import StringWidget, FileWidget
from openerp import fields, models

from dependencies.dependency import DisplayList
from dependencies.dependency import safe_unicode
from lims import PMF, bikaMessageFactory as _


#schema = Person.schema.copy() + Schema((
schema =  (
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
    
    fields.Char(compute='computeFulname', string='Fullname'),
    
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
      
    # ~~~~~~~ To be implemented ~~~~~~~
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
    # ~~~~~~~ To be implemented ~~~~~~~
    #  LinesField('PublicationPreference',
    #     vocabulary = PUBLICATION_PREFS,
    #     default = 'email',
    #     schemata = 'Publication preference',
    #     widget = MultiSelectionWidget(
    #         label=_("Publication preference"),
    #     ),
    # ),
    FileField('Signature',
              help="Upload a scanned signature to be used on printed analysis results reports."+
               "Ideal size is 250 pixels wide by 150 high",
               widget = FileWidget(
               label = _("Signature"),
        ),
    ),
    # ImageField('Signature',
    #     widget = ImageWidget(
    #         label=_("Signature"),
    #         description = _(
    #             "Upload a scanned signature to be used on printed analysis "
    #             "results reports. Ideal size is 250 pixels wide by 150 high"),
    #     ),
    # ),
 fields.Many2many(string='Department',
                       comodel_name='olims.department',
#         schemata = 'Publication preference',
#         vocabulary = 'getContacts',
#         multiValued = 1,
#         allowed_types = ('Contact',),
#         relationship = 'ContactContact',
#         widget = ReferenceWidget(
#             checkbox_bound = 0,
#             label=_("Contacts to CC"),
#         ),
        ),
    # ReferenceField('Department',
    #     required = 0,
    #     vocabulary_display_path_bound = sys.maxint,
    #     allowed_types = ('Department',),
    #     relationship = 'LabContactDepartment',
    #     vocabulary = 'getDepartments',
    #     referenceClass = HoldingReference,
    #     widget = ReferenceWidget(
    #         checkbox_bound = 0,
    #         label=_("Department"),
    #         description=_("The laboratory department"),
    #     ),
    # ),

    # ~~~~~~~ To be implemented ~~~~~~~
    # ComputedField('DepartmentTitle',
    #     expression = "context.getDepartment() and context.getDepartment().Title() or ''",
    #     widget = ComputedWidget(
    #         visible = False,
    #     ),
    # ),
)
#
# schema['JobTitle'].schemata = 'default'
# # Don't make title required - it will be computed from the Person's Fullname
# schema['title'].required = 0
# schema['title'].widget.visible = False

class LabContact(models.Model, BaseOLiMSModel): #Person
    _name = 'olims.lab_contact'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema
    # implements(ILabContact)

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
            record.Fullname = fullname.strip()
    

    def Title(self):
        """ Return the contact's Fullname as title """
        return safe_unicode(self.getFullname()).encode('utf-8')

    def hasUser(self):
        """ check if contact has user """
        return self.portal_membership.getMemberById(
            self.getUsername()) is not None

    def getDepartments(self):
        bsc = getToolByName(self, 'bika_setup_catalog')
        items = [('','')] + [(o.UID, o.Title) for o in
                               bsc(portal_type='Department',
                                   inactive_state = 'active')]
        o = self.getDepartment()
        if o and o.UID() not in [i[0] for i in items]:
            items.append((o.UID(), o.Title()))
        items.sort(lambda x,y: cmp(x[1], y[1]))
        return DisplayList(list(items))

#registerType(LabContact, PROJECTNAME)

LabContact.initialze(schema)