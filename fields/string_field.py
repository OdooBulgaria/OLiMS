from openerp import fields
import logging

from fields_utils import boolean_value_base_mapper, direct_mapper


_logger = logging.getLogger(__name__)

class StringField(fields.Char):
#    type = 'char' will auto inherit from the base class of Char
        
    def __bika_2_odoo_attrs_mapping(self):
        boolean_value_base_mapper(self, 'required', 1, 'required', True, False)
        boolean_value_base_mapper(self, 'searchable', 1, 'search', True, False)
        direct_mapper(self, 'description', 'help')
        
    def _setup_regular(self, env):
        super(StringField, self)._setup_regular(env)
        _logger.warning('***** GOT sample_field::self._attrs: %r ****' % self._attrs)
        
        self.__bika_2_odoo_attrs_mapping()

        _logger.warning('***** AFTER MAPPING sample_field::self._attrs: %r ****' % self._attrs)
        
    pass
