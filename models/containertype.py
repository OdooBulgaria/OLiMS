# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import *
# from dependencies.dependency import getToolByName
# from lims.utils import t
# from lims.content.bikaschema import BikaSchema
# from lims.config import PROJECTNAME
from openerp import models
from fields.string_field import StringField
from fields.text_field import TextField
from fields.widget.widget import StringWidget, TextAreaWidget
from models.base_olims_model import BaseOLiMSModel
from lims import bikaMessageFactory as _
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema = BikaSchema.copy() + Schema((
# ))
schema = (StringField('name',
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
    )
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# schema['description'].widget.visible = True
# schema['description'].schemata = 'default'

class ContainerType(models.Model, BaseOLiMSModel):#(BaseContent):
    _name = 'olims.container_type'
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
#     security = ClassSecurityInfo()
#     displayContentsTab = False
#     schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)
# ~~~~~~~ To be implemented ~~~~~~~
#     def getContainers(self):
#         """Return a list of all containers of this type
#         """
#         _containers = []
#         for container in self.bika_setup.bika_containers.objectValues():
#             containertype = container.getContainerType()
#             if containertype and containertype.UID() == self.UID():
#                 _containers.append(container)
#         return _containers
# 
# registerType(ContainerType, PROJECTNAME)

ContainerType.initialze(schema)
# ~~~~~~~ To be implemented ~~~~~~~
# def ContainerTypes(self, instance=None, allow_blank=False):
#     instance = instance or self
#     bsc = getToolByName(instance, 'bika_setup_catalog')
#     items = []
#     for o in bsc(portal_type='ContainerType',
#                  sort_on = 'sortable_title'):
#         items.append((o.UID, o.Title))
#     items = allow_blank and [['','']] + list(items) or list(items)
#     return DisplayList(items)
