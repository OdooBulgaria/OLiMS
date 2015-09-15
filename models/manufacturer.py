# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import *
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema
# from lims.interfaces import IManufacturer
# from dependencies.dependency import implements

import logging

from openerp import fields, models,osv

_logger = logging.getLogger(__name__)

from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.text_field import TextField
from fields.widget.widget import  TextAreaWidget
from lims import bikaMessageFactory as _

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema = BikaSchema.copy()
schema = (StringField(string='Title',
              required=1,        
    ),
    TextField(string='Description',
              widget=TextAreaWidget(
                label=_('Description'),
                description=_('Used in item listings and search results.')),    
    ),
    )
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['description'].schemata = 'default'
# schema['description'].widget.visible = True


class Manufacturer(models.Model, BaseOLiMSModel):#(BaseContent):
    _name = 'olims.manufacturer'
    
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~    
#     implements(IManufacturer)
#     security = ClassSecurityInfo()
#     displayContentsTab = False
#     schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)
        
Manufacturer.initialze(schema)

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# registerType(Manufacturer, PROJECTNAME)
