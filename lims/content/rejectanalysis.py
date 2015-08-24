""" RejectAnalysis """
from OLiMS.dependencies.dependency import ReferenceField, Schema, registerType
from OLiMS.lims.content.analysis import Analysis
from OLiMS.lims.config import PROJECTNAME
from OLiMS.lims.content.analysis import schema as analysis_schema


schema = analysis_schema + Schema((
    # The analysis that was originally rejected
    ReferenceField('Analysis',
        allowed_types=('Analysis',),
        relationship = 'RejectAnalysisAnalysis',
    ),
))

class RejectAnalysis(Analysis):
    archetype_name = 'RejectAnalysis'

    schema = schema


registerType(RejectAnalysis, PROJECTNAME)
