
import logging

from openerp import fields, models,osv
from models.base_olims_model import BaseOLiMSModel

_logger = logging.getLogger(__name__)

schema = (
          fields.Char(string='name', required=True),
          )

class Country(models.Model, BaseOLiMSModel):
    _name='olims.country'
    
Country.initialze(schema)
