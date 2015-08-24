from OLiMS.dependencies.dependency import implements
from OLiMS.dependencies.dependency import atapi
from OLiMS.dependencies.dependency import BaseContent
from OLiMS.lims.interfaces import IMultifile
from OLiMS.lims.content.bikaschema import BikaSchema
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims import config


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
