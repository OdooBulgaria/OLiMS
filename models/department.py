"""Department - the department in the laboratory.
"""
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import *
# from dependencies.dependency import HoldingReference
# from lims.content.bikaschema import BikaSchema
# from dependencies.dependency import ClassSecurityInfo
# from lims.utils import t
# from dependencies.dependency import implements

import logging

from openerp import fields, models,osv

_logger = logging.getLogger(__name__)

import sys
from lims import bikaMessageFactory as _
from dependencies.dependency import getToolByName
from lims.config import PROJECTNAME
# from dependencies.fields import StringField, TextField, ReferenceField
from fields.string_field import StringField
from fields.reference_field import ReferenceField
from fields.text_field import TextField
from fields.widget.widget import StringWidget, TextAreaWidget, ReferenceWidget
from models.base_olims_model import BaseOLiMSModel

# schema = BikaSchema.copy() + Schema(
schema = (
    StringField('name',
        required=1,
        widget=StringWidget(
            label=_('Title'),
            description=_('Title is required.'),
        ),
    ),
    TextField('Description',
        widget=TextAreaWidget(
            label=_('Description'),
            description=_('Used in item listings and search results.'),
        ),
    ),

    ReferenceField(string='Manager',
           selection=[('olims.lab_contact', 'Manager')],
           required=1,
#         vocabulary = 'getContacts',
#         vocabulary_display_path_bound = sys.maxint,
#         allowed_types = ('LabContact',),
# #         referenceClass = HoldingReference,
#         relationship = 'DepartmentLabContact',
#         widget = ReferenceWidget(
#             checkbox_bound = 0,
#             label=_("Manager"),
#             description = _(
#                 "Select a manager from the available personnel configured under the "
#                 "'lab contacts' setup item. Departmental managers are referenced on "
#                 "analysis results reports containing analyses by their department."),
#         ),
    ),

# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('ManagerName',
#         expression = "context.getManager() and context.getManager().getFullname() or ''",
#         widget = ComputedWidget(
#             visible = False,
#         ),
#     ),

# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('ManagerPhone',
#         expression = "context.getManager() and context.getManager().getBusinessPhone() or ''",
#         widget = ComputedWidget(
#             visible = False,
#         ),
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('ManagerEmail',
#         expression = "context.getManager() and context.getManager().getEmailAddress() or ''",
#         widget = ComputedWidget(
#             visible = False,
#         ),
#     ),
)#)

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['description'].widget.visible = True
# schema['description'].schemata = 'default'


class Department(models.Model, BaseOLiMSModel):
    _name = 'olims.department'
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#     security = ClassSecurityInfo()
#     displayContentsTab = False
#     schema = schema
        
    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

Department.initialze(schema)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# registerType(Department, PROJECTNAME)
