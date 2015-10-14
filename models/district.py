
import logging

from openerp import fields, models,osv
from models.base_olims_model import BaseOLiMSModel

_logger = logging.getLogger(__name__)

schema = (
          fields.Many2one(comodel_name='olims.country',string='Country', required=True),
          fields.Many2one(comodel_name='olims.state',string='State',domain="[('Country', '=', Country)]", required=True),
          fields.Char(string='name', required=True),
          )

class District(models.Model, BaseOLiMSModel):
    _name='olims.district'
    
District.initialze(schema)
