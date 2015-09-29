# # ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#
# from dependencies.dependency import DateTime
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import UniqueObject
# from dependencies.dependency import View
# from dependencies import folder
# from dependencies.dependency import *
# from dependencies.dependency import safe_unicode
# from lims.content.organisation import Organisation
# from lims.config import ManageBika, PROJECTNAME


from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.integer_field import IntegerField
from fields.boolean_field import BooleanField
from fields.widget.widget import StringWidget, BooleanWidget,IntegerWidget
from dependencies.dependency import safe_unicode
from lims import PMF, bikaMessageFactory as _

#schema = Organisation.schema.copy() + Schema((
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

    StringField('LabURL',
        schemata = 'Address',
        #write_permission = ManageBika,
        widget = StringWidget(
            size = 60,
            label=_("Lab URL"),
            description=_("The Laboratory's web address"),
        ),
    ),
    IntegerField('Confidence',
        schemata = 'Accreditation',
        widget = IntegerWidget(
            label=_("Confidence Level %"),
            description=_("This value is reported at the bottom of all published results"),
        ),
    ),
    BooleanField('LaboratoryAccredited',
        default = False,
        schemata = 'Accreditation',
        #write_permission = ManageBika,
        widget = BooleanWidget(
            label=_("Laboratory Accredited"),
            description=_("Check this box if your laboratory is accredited"),
        ),
    ),
    StringField('AccreditationBody',
        schemata = 'Accreditation',
        #write_permission = ManageBika,
        widget = StringWidget(
            label=_("Accreditation Body Abbreviation"),
            description=_("E.g. SANAS, APLAC, etc."),
        ),
    ),
    StringField('AccreditationBodyURL',
        schemata = 'Accreditation',
        #write_permission = ManageBika,
        widget = StringWidget(
            label=_("Accreditation Body URL"),
            description=_("Web address for the accreditation body"),
        ),
    ),
    StringField('Accreditation',
        schemata = 'Accreditation',
        #write_permission = ManageBika,
        widget = StringWidget(
            label=_("Accreditation"),
            description=_("The accreditation standard that applies, e.g. ISO 17025"),
        ),
    ),
    StringField('AccreditationReference',
        schemata = 'Accreditation',
        #write_permission = ManageBika,
        widget = StringWidget(
            label=_("Accreditation Reference"),
            description=_("The reference code issued to the lab by the accreditation body"),
        ),
    ),
# ~~~~~~~ To be implemented ~~~~~~~
    # ImageField('AccreditationBodyLogo',
    #     schemata = 'Accreditation',
    #     widget = ImageWidget(
    #         label=_("Accreditation Logo"),
    #         description = _(
    #             "Please upload the logo you are authorised to use on your "
    #             "website and results reports by your accreditation body. "
    #             "Maximum size is 175 x 175 pixels.")
    #     ),
    # ),
    fields.Text('AccreditationPageHeader', size=10, help="Enter the details of your lab`s service accreditations "+
                "here.  The following fields are available:  lab_is_accredited, "+
                "lab_name, lab_country, confidence, accreditation_body_name, "+
                "accreditation_standard, accreditation_reference<br/>"
    # TextField('AccreditationPageHeader',
    #     schemata = 'Accreditation',
    #     default = "${lab_name} has been accredited as ${accreditation_standard} conformant by ${accreditation_body_abbr}, ${accreditation_body_name}<br/><br/>" + \
    #               "${accreditation_body_abbr} is the single national accreditation body assessing testing and calibration laboratories for compliance to the ISO/IEC 17025 standard.<br/></br/>\n" + \
    #               "The following analysis services have been included in the ${accreditation_body_abbr} schedule of Accreditation for this Laboratory:",
    #     widget = TextAreaWidget(
    #         label=_("Accreditation page header"),
    #         description = _(
    #             "Enter the details of your lab's service accreditations "
    #             "here.  The following fields are available:  lab_is_accredited, "
    #             "lab_name, lab_country, confidence, accreditation_body_name, "
    #             "accreditation_standard, accreditation_reference<br/>"),
    #             rows = 10
    #     ),
    ),

)


# # ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# IdField = schema['id']
# IdField.widget.visible = {'edit':'hidden', 'view': 'invisible'}
#
# schema['Name'].validators = ()
# # Update the validation layer after change the validator in runtime
# schema['Name']._validationLayer()

class Laboratory(models.Model, BaseOLiMSModel): #UniqueObject, Organisation
    _name='olims.laboratory'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    #security.declareProtected(View, 'getSchema')
    def getSchema(self):
        return self.schema

    def Title(self):
        title = self.getName() and self.getName() or _("Laboratory")
        return safe_unicode(title).encode('utf-8')

#registerType(Laboratory, PROJECTNAME)

Laboratory.initialze(schema)