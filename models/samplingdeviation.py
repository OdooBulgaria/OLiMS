# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import *
# from dependencies.dependency import HoldingReference
# from dependencies.dependency import RecordsField as RecordsField
# from lims.browser.widgets import RecordsWidget
# from lims.content.bikaschema import BikaSchema
# from lims.config import PROJECTNAME
# import sys
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from dependencies.dependency import implements
#

from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel
# from fields.string_field import StringField
# from fields.boolean_field import BooleanField
# from fields.date_time_field import DateTimeField

#
# schema = BikaSchema.copy() + Schema((
#
# ))

schema = ()

# schema['description'].schemata = 'default'
# schema['description'].widget.visible = True

class SamplingDeviation(models.Model, BaseOLiMSModel): #BaseFolder
    _name = 'olims.sampling_deviation'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

#registerType(SamplingDeviation, PROJECTNAME)
SamplingDeviation.initialze(schema)