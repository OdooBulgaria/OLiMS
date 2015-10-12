
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~

#from dependencies.dependency import ClassSecurityInfo
#from lims.content.bikaschema import BikaSchema
#from lims.interfaces import IInvoice
#from dependencies.dependency import DateTimeField, DateTimeWidget
#from dependencies.dependency import DateTime
#from dependencies.dependency import implements
#from lims.config import ManageInvoices, ManageBika, PROJECTNAME\
#from dependencies.dependency import PersistentMapping
#from dependencies.dependency import View

from dependencies.dependency import Decimal
from dependencies.dependency import getToolByName
from dependencies.dependency import safe_unicode
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.utils import to_utf8


from datetime import date
from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.text_field import TextField
from fields.boolean_field import BooleanField
from fields.date_time_field import DateTimeField
from fields.file_field import FileField
from fields.reference_field import ReferenceField
from fields.widget.widget import StringWidget, TextAreaWidget, BooleanWidget, FileWidget, DateTimeWidget

import logging
import sys
_logger = logging.getLogger(__name__)


#schema = BikaSchema.copy() + Schema((
schema = (
    # ~~~~~~~ To be implemented ~~~~~~~
    # ReferenceField('Client',
    #     required=1,
    #     vocabulary_display_path_bound=sys.maxsize,
    #     allowed_types=('Client',),
    #     relationship='ClientInvoice',
    # ),
    # ReferenceField('AnalysisRequest',
    #     required=1,
    #     vocabulary_display_path_bound=sys.maxsize,
    #     allowed_types=('AnalysisRequest',),
    #     relationship='AnalysisRequestInvoice',
    # ),

    DateTimeField('InvoiceDate',
        required=1,
        default_method='current_date',
        widget=DateTimeWidget(
            label=_("Date"),
        ),
    ),
    TextField('Remarks',
        searchable=True,
        #default_content_type='text/plain',
        #allowed_content_types=('text/plain', ),
        #default_output_type="text/plain",
        widget=TextAreaWidget(
         #   macro="bika_widgets/remarks",
            label=_("Remarks"),
            append_only=True,
        ),
    ),
    
    fields.Float(compute='getSubtotal', string='subtotal'),
          
    # ~~~~~~~ To be implemented ~~~~~~~
    # ComputedField('Subtotal',
    #     expression='context.getSubtotal()',
    #     widget=ComputedWidget(
    #         label=_("Subtotal"),
    #         visible=False,
    #     ),
    # ),
    fields.Float(compute='getVATAmount', string='VATAmount'),
    # ComputedField('VATAmount',
    #     expression='context.getVATAmount()',
    #     widget=ComputedWidget(
    #         label=_("VAT Total"),
    #         visible=False,
    #     ),
    # ),
    # ComputedField('Total',
    #     expression='context.getTotal()',
    #     widget=ComputedWidget(
    #         label=_("Total"),
    #         visible=False,
    #     ),
    # ),
    # ComputedField('ClientUID',
    #     expression='here.getClient() and here.getClient().UID()',
    #     widget=ComputedWidget(
    #         visible=False,
    #     ),
    # ),
    # ComputedField('InvoiceSearchableText',
    #     expression='here.getInvoiceSearchableText()',
    #     widget=ComputedWidget(
    #         visible=False,
    #     ),
    # ),
)

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# TitleField = schema['title']
# TitleField.required = 0
# TitleField.widget.visible = False


# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# class InvoiceLineItem(PersistentMapping):
#     pass


class Invoice(models.Model, BaseOLiMSModel): #(BaseFolder):
    _name='olims.invoice'
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
    # implements(IInvoice)
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def Title(self):
        """ Return the Invoice Id as title """
        return safe_unicode(self.getId()).encode('utf-8')

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
    #security.declareProtected(View, 'getSubtotal')

    def getSubtotal(self):
        """ Compute Subtotal """
        for record in self:
            total = sum([float(obj['Subtotal']) for obj in record.invoice_lineitems])
            record.subtotal = total
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
    #security.declareProtected(View, 'getVATAmount')

    def getVATAmount(self):
        """ Compute VAT """
        for record in self:
            
            record.VATAmount = Decimal(record.getTotal()) - Decimal(record.getSubtotal())

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
    #security.declareProtected(View, 'getTotal')

    def getTotal(self):
        """ Compute Total """
        total = sum([float(obj['Total']) for obj in self.invoice_lineitems])
        

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
    #security.declareProtected(View, 'getInvoiceSearchableText')

    def getInvoiceSearchableText(self):
        """ Aggregate text of all line items for querying """
        s = ''
        for item in self.invoice_lineitems:
            s = s + item['ItemDescription']
        return s

    # XXX workflow script
    def workflow_script_dispatch(self):
        """ dispatch order """
        self.setDateDispatched(DateTime())

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
    #security.declarePublic('current_date')

    def current_date(self):
        """ return current date """
        return DateTime()

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#registerType(Invoice, PROJECTNAME)
Invoice.initialze(schema)