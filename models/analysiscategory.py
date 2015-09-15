"""Analysis Category - the category of the analysis service
"""
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from lims.utils import t
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema
# from lims.interfaces import IAnalysisCategory
# from dependencies.dependency import implements
# from dependencies.dependency import HoldingReference
# from dependencies.dependency import DisplayList

import logging

from openerp import fields, models

_logger = logging.getLogger(__name__)
from lims import bikaMessageFactory as _
from dependencies.dependency import getToolByName
from dependencies.dependency import WorkflowException
from fields.string_field import StringField
from fields.text_field import TextField
from fields.widget.widget import TextAreaWidget
from models.base_olims_model import BaseOLiMSModel
import sys
from dependencies import transaction

# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema = BikaSchema.copy() + Schema(
schema =  (StringField('Title',
              required=1,        
    ),
    TextField('Description',
        widget=TextAreaWidget(
            description = _('Used in item listings and search results.'),
                            )
    ),
    TextField('Comments',
        default_output_type = 'text/plain',
        allowable_content_types = ('text/plain',),
        widget=TextAreaWidget (
            description = _("To be displayed below each Analysis "
                            "Category section on results reports."),
            label = _("Comments")),
    ),
# ~~~~~~~ Using Odoo fields.Reference ~~~~~~~
    fields.Reference(string='Department',
        selection=[('olims.department', 'Department')],
        required=True,
    ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('DepartmentTitle',
#         expression="context.getDepartment() and context.getDepartment().Title() or ''",
#         widget=ComputedWidget(
#             visible=False,
#         ),
#     ),
)
#)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['description'].widget.visible = True
# schema['description'].schemata = 'default'


class AnalysisCategory(models.Model, BaseOLiMSModel):
    _name = "olims.analysis_category"
    
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~    
#     implements(IAnalysisCategory)
#     security = ClassSecurityInfo()
#     displayContentsTab = False
#     schema = schema

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)
# ~~~~~~~ To be implemented ~~~~~~~
#     def getDepartments(self):
#         bsc = getToolByName(self, 'bika_setup_catalog')
#         deps = []
#         for d in bsc(portal_type='Department',
#                      inactive_state='active'):
#             deps.append((d.UID, d.Title))
#         return DisplayList(deps)

    def workflow_script_deactivat(self):
        # A instance cannot be deactivated if it contains services
        pu = getToolByName(self, 'plone_utils')
        bsc = getToolByName(self, 'bika_setup_catalog')
        ars = bsc(portal_type='AnalysisService', getCategoryUID=self.UID())
        if ars:
            message = _("Category cannot be deactivated because "
                        "it contains Analysis Services")
            pu.addPortalMessage(message, 'error')
            transaction.get().abort()
            raise WorkflowException

AnalysisCategory.initialze(schema)
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# registerType(AnalysisCategory, PROJECTNAME)
