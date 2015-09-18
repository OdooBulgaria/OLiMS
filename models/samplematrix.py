# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import *
# from dependencies.dependency import HoldingReference
# from dependencies.dependency import RecordsField as RecordsField
# from dependencies.dependency import getToolByName
# from lims.browser.widgets import RecordsWidget
# from lims.content.bikaschema import BikaSchema
# from lims.config import PROJECTNAME
# import sys
# from lims.utils import t
# from dependencies.dependency import implements
from openerp import fields, models
from lims import bikaMessageFactory as _
from fields.string_field import StringField
from fields.text_field import TextField
from fields.widget.widget import TextAreaWidget
from models.base_olims_model import BaseOLiMSModel
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema = BikaSchema.copy() + Schema((
# 
# ))
schema = (StringField('name',
              required=1,        
    ),
    TextField('Description',
              widget=TextAreaWidget(
                label=_('Description'),
                description=_('Used in item listings and search results.')),    
    ),
    )
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['description'].schemata = 'default'
# schema['description'].widget.visible = True

class SampleMatrix(models.Model, BaseOLiMSModel):#(BaseFolder):
    _name = 'olims.sample_matrix'
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#     security = ClassSecurityInfo()
#     displayContentsTab = False
#     schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)
SampleMatrix.initialze(schema)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# registerType(SampleMatrix, PROJECTNAME)

# ~~~~~~~ To be implemented ~~~~~~~
# def SampleMatrices(self, instance=None, allow_blank=False):
#     instance = instance or self
#     bsc = getToolByName(instance, 'bika_setup_catalog')
#     items = []
#     for sm in bsc(portal_type='SampleMatrix',
#                   inactive_state='active',
#                   sort_on = 'sortable_title'):
#         items.append((sm.UID, sm.Title))
#     items = allow_blank and [['','']] + list(items) or list(items)
#     return DisplayList(items)
