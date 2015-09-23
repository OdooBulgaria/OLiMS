""" RejectAnalysis """
# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ReferenceField, Schema, registerType
# from lims.content.analysis import Analysis
# from lims.config import PROJECTNAME
# from lims.content.analysis import schema as analysis_schema

from openerp import fields, models
from lims import bikaMessageFactory as _
from fields.string_field import StringField
from fields.boolean_field import BooleanField
from fields.fixed_point_field import FixedPointField
from fields.text_field import TextField
from fields.date_time_field import DateTimeField
from fields.integer_field import IntegerField
from fields.widget.widget import ComputedWidget, DateTimeWidget, \
                                IntegerWidget, DecimalWidget
from models.base_olims_model import BaseOLiMSModel

#schema = analysis_schema + Schema((
schema = (
# ~~~~~~~ To be implemented ~~~~~~~
#         HistoryAwareReferenceField('Service',
#         required=1,
#         allowed_types=('AnalysisService',),
#         relationship='AnalysisAnalysisService',
#         referenceClass=HoldingReference,
#         widget=ReferenceWidget(
#             label = _("Analysis Service"),
#         )
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     HistoryAwareReferenceField('Calculation',
#         allowed_types=('Calculation',),
#         relationship='AnalysisCalculation',
#         referenceClass=HoldingReference,
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ReferenceField('Attachment',
#         multiValued=1,
#         allowed_types=('Attachment',),
#         referenceClass = HoldingReference,
#         relationship = 'AnalysisAttachment',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     InterimFieldsField('InterimFields',
#         widget = BikaRecordsWidget(
#             label = _("Calculation Interim Fields"),
#         )
#     ),
    StringField('Result',
    ),
    DateTimeField('ResultCaptureDate',
        widget = ComputedWidget(
            visible=False,
        ),
    ),
    StringField('ResultDM',
    ),
    BooleanField('Retested',
        default = False,
    ),
# ~~~~~~~ To be implemented ~~~~~~~
#     DurationField('MaxTimeAllowed',
#         widget = DurationWidget(
#             label = _("Maximum turn-around time"),
#             description=_("Maximum time allowed for completion of the analysis. "
#                             "A late analysis alert is raised when this period elapses"),
#         ),
#     ),
    DateTimeField('DateAnalysisPublished',
        widget = DateTimeWidget(
            label = _("Date Published"),
        ),
    ),
    DateTimeField('DueDate',
        widget = DateTimeWidget(
            label = _("Due Date"),
        ),
    ),
    IntegerField('Duration',
        widget = IntegerWidget(
            label = _("Duration"),
        )
    ),
    IntegerField('Earliness',
        widget = IntegerWidget(
            label = _("Earliness"),
        )
    ),
    BooleanField('ReportDryMatter',
        default = False,
    ),
    StringField('Analyst',
    ),
    TextField('Remarks',
    ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ReferenceField('Instrument',
#         required = 0,
#         allowed_types = ('Instrument',),
#         relationship = 'AnalysisInstrument',
#         referenceClass = HoldingReference,
#     ),
#     ReferenceField('Method',
#         required = 0,
#         allowed_types = ('Method',),
#         relationship = 'AnalysisMethod',
#         referenceClass = HoldingReference,
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ReferenceField('SamplePartition',
#         required = 0,
#         allowed_types = ('SamplePartition',),
#         relationship = 'AnalysisSamplePartition',
#         referenceClass = HoldingReference,
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('ClientUID',
#         expression = 'context.aq_parent.aq_parent.UID()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('ClientTitle',
#         expression = 'context.aq_parent.aq_parent.Title()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('RequestID',
#         expression = 'context.aq_parent.getRequestID()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('ClientOrderNumber',
#         expression = 'context.aq_parent.getClientOrderNumber()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('Keyword',
#         expression = 'context.getService().getKeyword()',
#     ),
#     ComputedField('ServiceTitle',
#         expression = 'context.getService().Title()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('ServiceUID',
#         expression = 'context.getService().UID()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('SampleTypeUID',
#         expression = 'context.aq_parent.getSample().getSampleType().UID()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('SamplePointUID',
#         expression = 'context.aq_parent.getSample().getSamplePoint().UID() if context.aq_parent.getSample().getSamplePoint() else None',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('CategoryUID',
#         expression = 'context.getService().getCategoryUID()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('CategoryTitle',
#         expression = 'context.getService().getCategoryTitle()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('PointOfCapture',
#         expression = 'context.getService().getPointOfCapture()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('DateReceived',
#         expression = 'context.aq_parent.getDateReceived()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('DateSampled',
#         expression = 'context.aq_parent.getSample().getDateSampled()',
#     ),
# ~~~~~~~ To be implemented ~~~~~~~
#     ComputedField('InstrumentValid',
#         expression = 'context.isInstrumentValid()'
#     ),
    FixedPointField('Uncertainty',
        widget=DecimalWidget(
            label = _("Uncertainty"),
        ),
    ),
    StringField('DetectionLimitOperand',
    ),

    # The analysis that was originally rejected
    fields.Many2one(string='Analysis',
                        comodel_name='olims.analysis',
        # allowed_types=('Analysis',),
        # relationship = 'RejectAnalysisAnalysis',
        ),

)

class RejectAnalysis(models.Model, BaseOLiMSModel): #Analysis
    _name ='olims.reject_analysis'
    #archetype_name = 'RejectAnalysis'
    #schema = schema


#registerType(RejectAnalysis, PROJECTNAME)
RejectAnalysis.initialze(schema)