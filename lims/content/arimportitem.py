from lims import bikaMessageFactory as _
from lims.utils import t
from lims.content.bikaschema import BikaSchema
from lims.config import PROJECTNAME
from lims.interfaces import IARImportItem
from dependencies.dependency import schemata
from dependencies import atapi
from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import View #, \
#     ModifyPortalContent
from dependencies.dependency import *
from dependencies.dependency import HoldingReference
from dependencies.dependency import safe_unicode
from dependencies.dependency import implements

schema = BikaSchema.copy() + Schema((
    StringField('SampleName',
        widget = StringWidget(
            label = _("Sample"),
        )
    ),
    StringField('ClientRef',
        widget = StringWidget(
            label = _("Client Ref"),
        )
    ),
    StringField('ClientRemarks',
        widget = StringWidget(
            label = _("Client Remarks"),
        )
    ),
    StringField('ClientSid',
        widget = StringWidget(
            label = _("Client SID"),
        )
    ),
    StringField('SampleType',
        widget = StringWidget(
            label = _("Sample Type"),
        )
    ),
    StringField('SampleDate',
        widget = StringWidget(
            label = _("Sample Date"),
        )
    ),
    StringField('NoContainers',
        widget = StringWidget(
            label = _("No of containers"),
        )
    ),
    StringField('PickingSlip',
        widget = StringWidget(
            label = _("Picking Slip"),
        )
    ),
    StringField('ContainerType',
        widget = StringWidget(
            label = _("Container Type"),
        )
    ),
    StringField('ReportDryMatter',
        widget = StringWidget(
            label = _("Report as Dry Matter"),
        )
    ),
    StringField('Priority',
        widget = StringWidget(
            label = _("Priority"),
        )
    ),
    LinesField('AnalysisProfile',
        widget = LinesWidget(
            label = _("Analysis Profile"),
        )
    ),
    LinesField('Analyses',
        widget = LinesWidget(
            label = _("Analyses"),
        )
    ),
    LinesField('Remarks',
        widget = LinesWidget(
            label = _("Remarks"),
            visible = {'edit':'hidden'},
        )
    ),
    ReferenceField('AnalysisRequest',
        allowed_types = ('AnalysisRequest',),
        relationship = 'ARImportItemAnalysisRequest',
        widget = ReferenceWidget(
            label = _("AnalysisProfile Request"),
            visible = {'edit':'hidden'},
        ),
    ),
    ReferenceField('Sample',
        allowed_types = ('Sample',),
        relationship = 'ARImportItemSample',
        widget = ReferenceWidget(
            label = _("Sample"),
            visible = {'edit':'hidden'},
        ),
    ),
),
)

class ARImportItem(BaseContent):
    security = ClassSecurityInfo()
    implements (IARImportItem)
    schema = schema
    displayContentsTab = False

    def Title(self):
        """ Return the Product as title """
        return safe_unicode(self.getSampleName()).encode('utf-8')


atapi.registerType(ARImportItem, PROJECTNAME)
