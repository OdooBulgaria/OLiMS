# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from lims.utils import t
# from lims.content.bikaschema import BikaSchema
# from lims.config import PROJECTNAME
# from lims.interfaces import IARPriority
# from dependencies import atapi
# from dependencies.dependency import *
# from dependencies.dependency import implements

import logging
from openerp import models

_logger = logging.getLogger(__name__)

from lims.idserver import renameAfterCreation
from lims import bikaMessageFactory as _
from models.base_olims_model import BaseOLiMSModel
from fields.integer_field import IntegerField
from fields.file_field import FileField
from fields.boolean_field import BooleanField
from fields.widget.widget import IntegerWidget, BooleanWidget, FileWidget
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema = BikaSchema.copy() + Schema((
schema = (IntegerField('sortKey',
        widget=IntegerWidget(
            label = _("Sort Key"),
            description = _("Numeric value indicating the sort order of objects that are prioritised"),
        ),
    ),
    IntegerField('pricePremium',
        widget=IntegerWidget(
            label = _("Price Premium Percentage"),
            description = _("The percentage used to calculate the price for analyses done at this priority"),
        ),
    ),
          
    FileField('smallIcon',
              help='6x16 pixel icon used for the this priority in listings.',
              widget = FileWidget(
              label = _("Small Icon"),
              ),
    ),
          
    FileField('bigIcon',
              help='32x32 pixel icon used for the this priority in object views.',
              widget = FileWidget(
              label = _("Big Icon"),
              ),
    ),
         
    BooleanField('isDefault',
        widget=BooleanWidget(
            label = _("Default Priority?"),
            description = _("Check this box if this is the default priority"),
        ),
    ),
)#)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['description'].widget.visible = True


class ARPriority(models.Model, BaseOLiMSModel):#(BaseContent):
    _name = 'olims.ar_priority'
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#     security = ClassSecurityInfo()
#     schema = schema
#     displayContentsTab = False
#     implements(IARPriority)
#     _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        renameAfterCreation(self)

ARPriority.initialze(schema)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# atapi.registerType(ARPriority, PROJECTNAME)
