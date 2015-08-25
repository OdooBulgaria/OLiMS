from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t
from OLiMS.lims.content.bikaschema import BikaSchema
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims.interfaces import IARImportItem
from OLiMS.dependencies.dependency import schemata
from OLiMS.dependencies import atapi
from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import View #, \
#     ModifyPortalContent
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import HoldingReference
from OLiMS.dependencies.dependency import safe_unicode
from OLiMS.dependencies.dependency import implements

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
