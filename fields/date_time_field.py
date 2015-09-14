from openerp import fields
import logging

# from fields_utils import direct_mapper


_logger = logging.getLogger(__name__)

class DateTimeField(fields.Datetime):
#    type = 'datetime' will auto inherit from the base class of Datetime
        
#     def __bika_2_odoo_attrs_mapping(self):
#         direct_mapper(self, 'description', 'help')
        
    def _setup_regular(self, env):
        super(DateTimeField, self)._setup_regular(env)
#         self.__bika_2_odoo_attrs_mapping()
        
    pass