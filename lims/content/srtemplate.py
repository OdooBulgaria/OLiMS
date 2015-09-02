"""
    Sample Round Template
"""

from dependencies.dependency import ClassSecurityInfo
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.browser.widgets import RecordsWidget as BikaRecordsWidget
from lims.browser.widgets import SRTemplateARTemplatesWidget
from lims.config import PROJECTNAME
from lims.content.bikaschema import BikaSchema
from lims.idserver import renameAfterCreation
from dependencies.dependency import *
from dependencies.dependency import RecordsField
from dependencies.dependency import getToolByName


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
