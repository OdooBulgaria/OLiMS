
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import schemata
# from dependencies import atapi
# from dependencies.dependency import *
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from lims.browser.widgets import DateTimeWidget, ReferenceWidget
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema
# from dependencies.dependency import permissions


from lims import bikaMessageFactory as _
from fields.string_field import StringField
from fields.text_field import TextField
from fields.date_time_field import DateTimeField
from fields.reference_field import ReferenceField
from fields.boolean_field import BooleanField
from fields.widget.widget import StringWidget, TextAreaWidget, DateTimeWidget, BooleanWidget
from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel

#schema = BikaSchema.copy() + Schema((
schema = (
    # ComputedField('AssetNumber',
    #     expression='here.getInstrumentAssetNumber()',
    #     widget=ComputedWidget(
    #         label=_('Instrument Asset Number'),
    #         visible=True,
    #         description=_("Instrument's Asset Number")
    #      )
    # ),

        fields.Many2one(string='Instrument',
                   comodel_name='olims.instrument',
          #allowed_types=('Instrument',),
        #relationship='InstrumentCertificationInstrument',
     #   widget=StringWidget(
     #       visible=False,
     #   ),
    ),

    # ComputedField('InstrumentUID',
    #     expression = 'context.getInstrument() and context.getInstrument().UID() or None',
    #     widget=ComputedWidget(
    #         visible=False,
    #     ),
    # ),

    # Set the Certificate as Internal
    # When selected, the 'Agency' field is hidden
    BooleanField('Internal',
        default=False,
        widget=BooleanWidget(
            label=_("Internal Certificate"),
            description=_("Select if is an in-house calibration certificate")
        )
    ),

    StringField('Agency',
        widget = StringWidget(
            label=_("Agency"),
            description=_("Organization responsible of granting the calibration certificate")
        ),
    ),

    DateTimeField('Date',
        widget = DateTimeWidget(
            label=_("Date"),
            description=_("Date when the calibration certificate was granted"),
        ),
    ),

    DateTimeField('ValidFrom',
        with_time = 1,
        with_date = 1,
        required = 1,
        widget = DateTimeWidget(
            label=_("From"),
            description=_("Date from which the calibration certificate is valid"),
        ),
    ),

    DateTimeField('ValidTo',
        with_time = 1,
        with_date = 1,
        required = 1,
        widget = DateTimeWidget(
            label=_("To"),
            description=_("Date until the certificate is valid"),
        ),
    ),

    fields.Many2one(string='Preparator',
                   comodel_name='olims.lab_contact',
                   help="The person at the supplier who prepared the certificate",
#               vocabulary='getLabContacts',
    #     allowed_types=('LabContact',),
    #     relationship='LabContactInstrumentCertificatePreparator',
    #     widget=ReferenceWidget(
    #         checkbox_bound=0,
    #         label=_("Prepared by"),
    #         description=_("The person at the supplier who prepared the certificate"),
    #         size=30,
    #         base_query={'inactive_state': 'active'},
    #         showOn=True,
    #         colModel=[{'columnName': 'UID', 'hidden': True},
    #                   {'columnName': 'JobTitle', 'width': '20', 'label': _('Job Title')},
    #                   {'columnName': 'Title', 'width': '80', 'label': _('Name')}
    #                  ],
    #     ),
    ),

    fields.Many2one(string='Validator',
                   comodel_name='olims.lab_contact',
                   help="The person at the supplier who approved the certificate"
    #     vocabulary='getLabContacts',
    #     allowed_types=('LabContact',),
    #     relationship='LabContactInstrumentCertificateValidator',
    #     widget=ReferenceWidget(
    #         checkbox_bound=0,
    #         label=_("Approved by"),
    #         description=_("The person at the supplier who approved the certificate"),
    #         size=30,
    #         base_query={'inactive_state': 'active'},
    #         showOn=True,
    #         colModel=[{'columnName': 'UID', 'hidden': True},
    #                   {'columnName': 'JobTitle', 'width': '20', 'label': _('Job Title')},
    #                   {'columnName': 'Title', 'width': '80', 'label': _('Name')}
    #                  ],
    #     ),
    ),



    # FileField('Document',
    #     widget = FileWidget(
    #         label=_("Report upload"),
    #         description=_("Load the certificate document here"),
    #     )
    # ),

    TextField('Remarks',
        searchable=True,
        default_content_type='text/x-web-intelligent',
        allowable_content_types = ('text/plain', ),
        default_output_type="text/plain",
        mode="rw",
        widget=TextAreaWidget(
            macro="bika_widgets/remarks",
            label=_("Remarks"),
            append_only=True,
        ),
    ),

)

#schema['title'].widget.label=_("Certificate Code")

class InstrumentCertification(models.Model, BaseOLiMSModel): #BaseFolder
    _name = 'olims.instrument_certification'
    # security = ClassSecurityInfo()
    # schema = schema
    # displayContentsTab = False

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def getLabContacts(self):
        bsc = getToolByName(self, 'bika_setup_catalog')
        # fallback - all Lab Contacts
        pairs = []
        for contact in bsc(portal_type='LabContact',
                           inactive_state='active',
                           sort_on='sortable_title'):
            pairs.append((contact.UID, contact.Title))
        return DisplayList(pairs)

    def getInstrumentAssetNumber(self):
        """
        Obtains the instrument's asset number
        :return: The asset number string
        """
        return self.aq_parent.getAssetNumber() if self.aq_parent.getAssetNumber() else ''

#atapi.registerType(InstrumentCertification, PROJECTNAME)
InstrumentCertification.initialze(schema)