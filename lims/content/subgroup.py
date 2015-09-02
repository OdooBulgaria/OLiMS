from dependencies.dependency import ClassSecurityInfo
from lims import bikaMessageFactory as _
from lims.utils import t
from lims.config import PROJECTNAME
from lims.interfaces import ISubGroup
from lims.content.bikaschema import BikaSchema
from lims.fields import *
from dependencies.dependency import *
from dependencies.dependency import implements

schema = BikaSchema.copy() + Schema((
    ExtStringField(
        'SortKey',
        widget=StringWidget(
            label=_("Sort Key"),
            description=_("Subgroups are sorted with this key in group views")
        )
    ),
))
schema['description'].widget.visible = True
schema['description'].schemata = 'default'


class SubGroup(BaseContent):
    implements(ISubGroup)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(SubGroup, PROJECTNAME)
