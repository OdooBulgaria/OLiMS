# from dependencies.dependency import ClassSecurityInfo
# from lims.utils import t
# from lims.browser.fields import DurationField
# from lims.browser.widgets import DurationWidget
# from lims.config import PROJECTNAME, PRESERVATION_CATEGORIES
# from lims.content.bikaschema import BikaSchema
# from lims.vocabularies import CatalogVocabulary
# from dependencies.dependency import *
# from dependencies.dependency import getToolByName
# from dependencies.dependency import  check as CheckAuthenticator

import json
from operator import itemgetter
from lims import bikaMessageFactory as _
from fields.string_field import StringField
from fields.text_field import TextField
from fields.widget.widget import StringWidget, TextAreaWidget
from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel
PRESERVATION_CATEGORIES = (
    ('field', _('Field Preservation')),
    ('lab', _('Lab Preservation')),
    )
# schema = BikaSchema.copy() + Schema(
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
    fields.Selection(string='Category',
        selection=PRESERVATION_CATEGORIES,
        default='lab',
#         vocabulary=PRESERVATION_CATEGORIES,
#         widget=SelectionWidget(
#             format='flex',
#             label=_("Preservation Category"),
#         ),
    ),
    
    fields.Char(string='Days'),
    fields.Char(string='Hours'),
    fields.Char(string='Minutes'),

)#)
# schema['description'].widget.visible = True
# schema['description'].schemata = 'default'


class Preservation(models.Model, BaseOLiMSModel):#(BaseContent):
    _name = 'olims.preservation'
#     security = ClassSecurityInfo()
#     displayContentsTab = False
#     schema = schema

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

Preservation.initialze(schema)
# registerType(Preservation, PROJECTNAME)


# class ajaxGetPreservations:
# 
#     catalog_name='bika_setup_catalog'
#     contentFilter = {'portal_type': 'Preservation',
#                      'inactive_state': 'active'}
# 
#     def __init__(self, context, request):
#         self.context = context
#         self.request = request
# 
#     def __call__(self):
# 
#         CheckAuthenticator(self.request)
#         searchTerm = 'searchTerm' in self.request and self.request[
#             'searchTerm'].lower() or ''
#         page = self.request['page']
#         nr_rows = self.request['rows']
#         sord = self.request['sord']
#         sidx = self.request['sidx']
#         rows = []
# 
#         # lookup objects from ZODB
#         catalog = getToolByName(self.context, self.catalog_name)
#         brains = catalog(self.contentFilter)
#         brains = searchTerm and \
#             [p for p in brains if p.Title.lower().find(searchTerm) > -1] \
#             or brains
# 
#         rows = [{'UID': p.UID,
#                  'preservation_uid': p.UID,
#                  'Preservation': p.Title,
#                  'Description': p.Description}
#                 for p in brains]
# 
#         rows = sorted(rows, cmp=lambda x, y: cmp(x.lower(
#         ), y.lower()), key=itemgetter(sidx and sidx or 'Preservation'))
#         if sord == 'desc':
#             rows.reverse()
#         pages = len(rows) / int(nr_rows)
#         pages += divmod(len(rows), int(nr_rows))[1] and 1 or 0
#         ret = {'page': page,
#                'total': pages,
#                'records': len(rows),
#                'rows': rows[(int(page) - 1) * int(nr_rows): int(page) * int(nr_rows)]}
#         return json.dumps(ret)
