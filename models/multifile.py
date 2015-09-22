# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import implements
# from dependencies import atapi
# from dependencies.dependency import BaseContent
# from lims.interfaces import IMultifile
# from lims.content.bikaschema import BikaSchema
# from lims import bikaMessageFactory as _
# from lims import config

from lims import bikaMessageFactory as _
from fields.string_field import StringField
from fields.widget.widget import StringWidget
from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel

#schema = BikaSchema.copy() + atapi.Schema((
schema = (
    StringField('DocumentID',
    required=1,
    validators=('uniquefieldvalidator',),
    widget = StringWidget(
        label=_("Document ID"),
        )
    ),
# ~~~~~~~ To be implemented ~~~~~~~
    # FileField('File',
    # required=1,
    # widget = FileWidget(
    #     label=_("Document"),
    #     description=_("File upload "),
    #     )
    # ),

    StringField('DocumentVersion',
    widget = StringWidget(
        label=_("Document Version"),
        )
    ),

    StringField('DocumentLocation',
    widget = StringWidget(
        label=_("Document Location"),
        description=_("Location where the document set is shelved"),
        )
    ),

    StringField('DocumentType',
    required=1,
    widget = StringWidget(
        label=_("Document Type"),
        description=_("Type of document (e.g. user manual, instrument specifications, image, ...)"),
        )
    ),
)

# TitleField = schema['title']
# TitleField.required = 0
# TitleField.widget.visible = False

class Multifile(models.Model, BaseOLiMSModel): #BaseContent
    _name = 'olims.multifile'
    # It implements the IEthnicity interface
    # implements(IMultifile)
    # schema = schema

# Activating the content type in Archetypes' internal types registry
#atapi.registerType(Multifile, config.PROJECTNAME)
Multifile.initialze(schema)