# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import *
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema
# from dependencies.dependency import Decimal
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from dependencies.dependency import implements

from lims import bikaMessageFactory as _
from fields.string_field import StringField

from fields.fixed_point_field import FixedPointField
from fields.widget.widget import StringWidget,DecimalWidget
from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel


#schema = BikaSchema.copy() + Schema((
schema = (StringField('Volume',
        widget = StringWidget(
            label=_("Volume"),
        )
    ),
    StringField('Unit',
        widget = StringWidget(
            label=_("Unit"),
        )
    ),
    FixedPointField('VAT',
        default_method = 'getDefaultVAT',
        widget = DecimalWidget(
            label=_("VAT %"),
            description=_("Enter percentage value eg. 14.0"),
        ),
    ),
    FixedPointField('Price',
        required=1,
        widget = DecimalWidget(
            label=_("Price excluding VAT"),
        )
    ),
    
    fields.Float(compute='computeVATAmount',string='VATAmount'),
# ~~~~~~~ To be implemented ~~~~~~~
    # ComputedField('VATAmount',
    #     expression = 'context.getVATAmount()',
    #     widget = ComputedWidget(
    #         label=_("VAT"),
    #         visible = {'edit':'hidden', }
    #     ),
    # ),
    fields.Float(compute='computeTotalPrice',string='TotalPrice'),
    # ComputedField('TotalPrice',
    #     expression = 'context.getTotalPrice()',
    #     widget = ComputedWidget(
    #         label=_("Total price"),
    #         visible = {'edit':'hidden', }
    #     ),
    # ),
)

# schema['description'].schemata = 'default'
# schema['description'].widget.visible = True

class LabProduct(models.Model, BaseOLiMSModel): #BaseContent
    _name ='olims.lab_product'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def computeTotalPrice(self):
        """ compute total price """
        for record in self:
            price = record.getPrice()
            price = int(price or '0.00')
            vat = int(record.getVAT())
            price = price and price or 0
            vat = vat and vat / 100 or 0
            price = price + (price * vat)
            record.TotalPrice = price       
    
#     def getTotalPrice(self):
#         """ compute total price """
#         price = self.getPrice()
#         price = Decimal(price or '0.00')
#         vat = Decimal(self.getVAT())
#         price = price and price or 0
#         vat = vat and vat / 100 or 0
#         price = price + (price * vat)
#         return price.quantize(Decimal('0.00'))

    def getDefaultVAT(self):
        """ return default VAT from bika_setup """
        try:
            vat = self.bika_setup.getVAT()
            return vat
        except ValueError:
            return "0.00"

    #security.declarePublic('getVATAmount')
    def computeVATAmount(self):
        """ Compute VATAmount
        """
        for record in self:
            try:
                vatamount = record.getTotalPrice() - record.getPrice()
            except:
                vatamount = 0
            record.VATAmount= vatamount

#registerType(LabProduct, PROJECTNAME)

LabProduct.initialze(schema)