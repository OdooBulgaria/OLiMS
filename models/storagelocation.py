# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import *
# from dependencies.dependency import HistoryAwareMixin
# from dependencies.dependency import getToolByName
# from dependencies.dependency import safe_unicode
# from lims.browser import BrowserView
# from lims.content.bikaschema import BikaSchema
# from lims.config import PROJECTNAME
# from lims.browser.fields import CoordinateField
# from lims.browser.widgets import CoordinateWidget
# from lims.browser.fields import DurationField
# from lims.browser.widgets import DurationWidget
# from lims import PMF, bikaMessageFactory as _
# from dependencies.dependency import implements
# import json
# import sys

#schema = BikaSchema.copy() + Schema((

from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel
from fields.string_field import StringField
from fields.widget.widget import StringWidget
from lims import bikaMessageFactory as _

schema =(
    StringField('SiteTitle',
        widget=StringWidget(
            label=_("Site Title"),
            description=_("Title of the site"),
        ),
    ),
    StringField('SiteCode',
        widget=StringWidget(
            label=_("Site Code"),
            description=_("Code for the site"),
        ),
    ),
    StringField('SiteDescription',
        widget=StringWidget(
            label=_("Site Description"),
            description=_("Description of the site"),
        ),
    ),
    StringField('LocationTitle',
        widget=StringWidget(
            label=_("Location Title"),
            description=_("Title of location"),
        ),
    ),
    StringField('LocationCode',
        widget=StringWidget(
            label=_("Location Code"),
            description=_("Code for the location"),
        ),
    ),
    StringField('LocationDescription',
        widget=StringWidget(
            label=_("Location Description"),
            description=_("Description of the location"),
        ),
    ),
    StringField('LocationType',
        widget=StringWidget(
            label=_("Location Type"),
            description=_("Type of location"),
        ),
    ),
    StringField('ShelfTitle',
        widget=StringWidget(
            label=_("Shelf Title"),
            description=_("Title of the shelf"),
        ),
    ),
    StringField('ShelfCode',
        widget=StringWidget(
            label=_("Shelf Code"),
            description=_("Code the the shelf"),
        ),
    ),
    StringField('ShelfDescription',
        widget=StringWidget(
            label=_("Shelf Description"),
            description=_("Description of the shelf"),
        ),
    ),
)

# schema['title'].widget.label=_('Address')
#schema['description'].widget.visible = True

class StorageLocation(models.Model, BaseOLiMSModel): #BaseContent, HistoryAwareMixin
    _name='olims.storage_location'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def Title(self):
        return safe_unicode(self.getField('title').get(self)).encode('utf-8')


#registerType(StorageLocation, PROJECTNAME)

StorageLocation.initialze(schema)