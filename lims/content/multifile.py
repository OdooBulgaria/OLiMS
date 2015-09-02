from dependencies.dependency import implements
from dependencies import atapi
from dependencies.dependency import BaseContent
from lims.interfaces import IMultifile
from lims.content.bikaschema import BikaSchema
from lims import bikaMessageFactory as _
from lims import config


schema = BikaSchema.copy() + atapi.Schema((

    atapi.StringField('DocumentID',
    required=1,
    validators=('uniquefieldvalidator',),
    widget = atapi.StringWidget(
        label=_("Document ID"),
        )
    ),

    atapi.FileField('File',
    required=1,
    widget = atapi.FileWidget(
        label=_("Document"),
        description=_("File upload "),
        )
    ),

    atapi.StringField('DocumentVersion',
    widget = atapi.StringWidget(
        label=_("Document Version"),
        )
    ),

    atapi.StringField('DocumentLocation',
    widget = atapi.StringWidget(
        label=_("Document Location"),
        description=_("Location where the document set is shelved"),
        )
    ),

    atapi.StringField('DocumentType',
    required=1,
    widget = atapi.StringWidget(
        label=_("Document Type"),
        description=_("Type of document (e.g. user manual, instrument specifications, image, ...)"),
        )
    ),
))

TitleField = schema['title']
TitleField.required = 0
TitleField.widget.visible = False

class Multifile(BaseContent):
    # It implements the IEthnicity interface
    implements(IMultifile)
    schema = schema

# Activating the content type in Archetypes' internal types registry
atapi.registerType(Multifile, config.PROJECTNAME)
