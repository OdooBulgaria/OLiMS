from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims.interfaces import ISubGroup
from OLiMS.lims.content.bikaschema import BikaSchema
from OLiMS.lims.fields import *
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import implements

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
        from OLiMS.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(SubGroup, PROJECTNAME)
