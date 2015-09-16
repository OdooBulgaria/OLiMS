from dependencies.dependency import ClassSecurityInfo
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.config import ManageInvoices, ManageBika, PROJECTNAME
from lims.content.bikaschema import BikaSchema
from lims.interfaces import IInvoice
from dependencies.dependency import DateTime
from dependencies.dependency import Decimal
from dependencies.dependency import PersistentMapping
from dependencies.dependency import *
from dependencies.dependency import DateTimeField, DateTimeWidget
from dependencies.dependency import View
from dependencies.dependency import safe_unicode
from dependencies.dependency import implements
import sys

schema = BikaSchema.copy() + Schema((
    ReferenceField('Client',
        required=1,
        vocabulary_display_path_bound=sys.maxsize,
        allowed_types=('Client',),
        relationship='ClientInvoice',
    ),
    ReferenceField('AnalysisRequest',
        required=1,
        vocabulary_display_path_bound=sys.maxsize,
        allowed_types=('AnalysisRequest',),
        relationship='AnalysisRequestInvoice',
    ),
    DateTimeField('InvoiceDate',
        required=1,
        default_method='current_date',
        widget=DateTimeWidget(
            label=_("Date"),
        ),
    ),
    TextField('Remarks',
        searchable=True,
        default_content_type='text/plain',
        allowed_content_types=('text/plain', ),
        default_output_type="text/plain",
        widget=TextAreaWidget(
            macro="bika_widgets/remarks",
            label=_("Remarks"),
            append_only=True,
        ),
    ),
    ComputedField('Subtotal',
        expression='context.getSubtotal()',
        widget=ComputedWidget(
            label=_("Subtotal"),
            visible=False,
        ),
    ),
    ComputedField('VATAmount',
        expression='context.getVATAmount()',
        widget=ComputedWidget(
            label=_("VAT Total"),
            visible=False,
        ),
    ),
    ComputedField('Total',
        expression='context.getTotal()',
        widget=ComputedWidget(
            label=_("Total"),
            visible=False,
        ),
    ),
    ComputedField('ClientUID',
        expression='here.getClient() and here.getClient().UID()',
        widget=ComputedWidget(
            visible=False,
        ),
    ),
    ComputedField('InvoiceSearchableText',
        expression='here.getInvoiceSearchableText()',
        widget=ComputedWidget(
            visible=False,
        ),
    ),
),
)

TitleField = schema['title']
TitleField.required = 0
TitleField.widget.visible = False


class InvoiceLineItem(PersistentMapping):
    pass


class Invoice(BaseFolder):
    implements(IInvoice)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def Title(self):
        """ Return the Invoice Id as title """
        return safe_unicode(self.getId()).encode('utf-8')

    security.declareProtected(View, 'getSubtotal')

    def getSubtotal(self):
        """ Compute Subtotal """
        return sum([float(obj['Subtotal']) for obj in self.invoice_lineitems])

    security.declareProtected(View, 'getVATAmount')

    def getVATAmount(self):
        """ Compute VAT """
        return Decimal(self.getTotal()) - Decimal(self.getSubtotal())

    security.declareProtected(View, 'getTotal')

    def getTotal(self):
        """ Compute Total """
        return sum([float(obj['Total']) for obj in self.invoice_lineitems])

    security.declareProtected(View, 'getInvoiceSearchableText')

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

    security.declarePublic('current_date')

    def current_date(self):
        """ return current date """
        return DateTime()

registerType(Invoice, PROJECTNAME)
