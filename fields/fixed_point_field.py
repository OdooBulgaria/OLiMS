from openerp import fields
import logging

from fields_utils import direct_mapper


_logger = logging.getLogger(__name__)

class FixedPointField(fields.Float):
#    type = 'float' will auto inherit from the base class of Float
        
    def __bika_2_odoo_attrs_mapping(self):
        
        _logger.warning('***** GOT sample_field::self._attrs: %r ****' % self._attrs)
        
#         string_to_float_mapper(self, 'default')
        direct_mapper(self, 'description', 'help')

        _logger.warning('***** AFTER MAPPING sample_field::self._attrs: %r ****' % self._attrs)
        
        
    def _setup_regular(self, env):
        super(FixedPointField, self)._setup_regular(env)
        self.__bika_2_odoo_attrs_mapping()
        
    pass