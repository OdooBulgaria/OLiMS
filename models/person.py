# # ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import rfc1123_date
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import permissions as CMFCorePermissions
# from dependencies.dependency import getToolByName
# from dependencies.dependency import *
# from lims.content.bikaschema import BikaSchema
# from dependencies.dependency import RecordWidget
# from lims.browser.widgets import AddressWidget
# from lims.config import GENDERS, PROJECTNAME
# from lims.browser.fields import AddressField


from openerp import fields, models
from fields.string_field import StringField
from models.base_olims_model import BaseOLiMSModel
from fields.widget.widget import StringWidget
from lims import bikaMessageFactory as _

#schema = BikaSchema.copy() + Schema((
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
          
    fields.Char(compute='computeFulname', string='Fullname'),
    # ~~~~~~~ To be implemented ~~~~~~~
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
        

)

class Person(models.Model, BaseOLiMSModel):#BaseFolder
    _name = 'olims.person'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

#    security.declareProtected(CMFCorePermissions.View, 'getSchema')
    def getSchema(self):
        return self.schema

    def getPossibleAddresses(self):
        return ['PhysicalAddress', 'PostalAddress']

    def computeFulname(self):
        """ return Person's Fullname """
        for record in self:
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
    
#     def getFullname(self):
#         """ return Person's Fullname """
#         
#         
#         fn = self.getFirstname()
#         mi = self.getMiddleinitial()
#         md = self.getMiddlename()
#         sn = self.getSurname()
#         fullname = ''
#         if fn or sn:
#             if mi and md:
#                 fullname = '%s %s %s %s' % (self.getFirstname(),
#                                         self.getMiddleinitial(),
#                                         self.getMiddlename(),
#                                         self.getSurname())
#             elif mi:
#                 fullname = '%s %s %s' % (self.getFirstname(),
#                                         self.getMiddleinitial(),
#                                         self.getSurname())
#             elif md:
#                 fullname = '%s %s %s' % (self.getFirstname(),
#                                         self.getMiddlename(),
#                                         self.getSurname())
#             else:
#                 fullname = '%s %s' % (self.getFirstname(), self.getSurname())
#         return fullname.strip()

    def getListingname(self):
        """ return Person's Fullname as Surname, Firstname """
        fn = self.getFirstname()
        mi = self.getMiddleinitial()
        md = self.getMiddlename()
        sn = self.getSurname()
        fullname = ''
        if fn and sn:
            fullname = '%s, %s' % (self.getSurname(), self.getFirstname())
        elif fn or sn:
            fullname = '%s %s' % (self.getSurname(), self.getFirstname())
        else:
            fullname = ''

        if fullname != '':
            if mi and md:
                fullname = '%s %s %s' % (fullname, self.getMiddleinitial(),
                                            self.getMiddlename())
            elif mi:
                fullname = '%s %s' % (fullname, self.getMiddleinitial())
            elif md:
                fullname = '%s %s' % (fullname, self.getMiddlename())

        return fullname.strip()

    #Title = getFullname

 #   security.declareProtected(CMFCorePermissions.ManagePortal, 'hasUser')
    def hasUser(self):
        """ check if contact has user """
        return self.portal_membership.getMemberById(
            self.getUsername()) is not None

    ### Removed these accessors to prevent confusion when LDAP is used
    # def getEmailAddress(self, **kw):
    #     """ Return the email address stored in member data if the
    #         person is a Plone user, else return the one stored on the
    #         person.
    #     """
    #     member = self.portal_membership.getMemberById(self.getUsername())
    #     if member:
    #         return member.getProperty('email')
    #     else:
    #         return self.Schema()['EmailAddress'].get(self)
    # def setEmailAddress(self, value, **kw):
    #     """ Set email in member data if the person is a Plone user, else
    #         store it on the Person instance.
    #     """
    #     self.Schema()['EmailAddress'].set(self, value, **kw)
    #     username = self.getUsername()
    #     if username:
    #         member = self.portal_membership.getMemberById(username)
    #         if member:
    #             member.setMemberProperties({'email': value})

#registerType(Person, PROJECTNAME)
Person.initialze(schema)