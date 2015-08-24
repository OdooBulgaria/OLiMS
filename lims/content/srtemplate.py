"""
    Sample Round Template
"""

from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.browser.widgets import RecordsWidget as BikaRecordsWidget
from OLiMS.lims.browser.widgets import SRTemplateARTemplatesWidget
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims.content.bikaschema import BikaSchema
from OLiMS.lims.idserver import renameAfterCreation
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import RecordsField
from OLiMS.dependencies.dependency import getToolByName


schema = BikaSchema.copy() + Schema((
    TextField('Instructions',
        searchable = True,
        default_content_type = 'text/plain',
        allowed_content_types= ('text/plain'),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            label=_("Instructions"),
            append_only = True,
        ),
    ),
    ReferenceField('ARTemplates',
        schemata = 'AR Templates',
        required = 1,
        multiValued = 1,
        allowed_types = ('ARTemplate',),
        relationship = 'SRTemplateARTemplate',
        widget = SRTemplateARTemplatesWidget(
            label=_("AR Templates"),
            description=_("Select AR Templates to include"),
        )
    ),
),
)


schema['description'].widget.visible = True
schema['title'].widget.visible = True
schema['title'].validators = ('uniquefieldvalidator',)
# Update the validation layer after change the validator in runtime
schema['title']._validationLayer()


class SRTemplate(BaseContent):
    security = ClassSecurityInfo()
    schema = schema
    displayContentsTab = False

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        renameAfterCreation(self)


registerType(SRTemplate, PROJECTNAME)
