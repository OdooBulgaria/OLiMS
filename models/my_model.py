from openerp import fields, models
import logging
from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.fixed_point_field import FixedPointField
from fields.widget.widget import StringWidget, DecimalWidget
from lims import bikaMessageFactory as _



_logger = logging.getLogger(__name__)


schema = (StringField('CommercialID', 
                        searchable=0, 
                        required=1, 
                        schemata='Accounting', 
                        tumbakto='blabla',
                        widget=StringWidget(
                            visible={'view': 'visible', 'edit': 'visible'},
                            label=_('Commercial ID'),
                            description=_("The profile's commercial ID for accounting purposes."),
                        ),
                ),

                StringField('MyTestField', searchable=1, required=0, schemata='Accounting',tumbakto='blabla'),
                
                StringField('NewField', searchable=1, required=1, schemata='Accounting',tumbakto='blabla'),
                FixedPointField('AnalysisProfilePrice',
                                schemata="Accounting",
                                default='0.00',
                                widget=DecimalWidget(
                                    label = _("Price (excluding VAT)"),
                                    description=_("Enter percentage value eg. 14.0. This percentage is applied on the Analysis Profile only, overriding "
                                                  "the systems VAT"),
                                    visible={'view': 'visible', 'edit': 'visible'},
        ),
    ),)
                
class MyModel(models.Model, BaseOLiMSModel):
    _name = 'mymodel.my_model'
        
                                    
MyModel.initialze(schema)
                    