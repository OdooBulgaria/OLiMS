from OLiMS.dependencies.dependency import ClassSecurityInfo
from OLiMS.dependencies.dependency import makeDisplayList
from OLiMS.dependencies.dependency import RecordField, RecordsField
from OLiMS.dependencies.dependency import registerField
from OLiMS.dependencies.dependency import *
from OLiMS.dependencies.dependency import getToolByName
from OLiMS.dependencies.dependency import validation
from OLiMS.dependencies.dependency import RegexValidator
import sys
from OLiMS.lims import bikaMessageFactory as _
from OLiMS.lims.utils import t


class ReferenceResultsField(RecordsField):

    """a list of reference sample results """
    _properties = RecordsField._properties.copy()
    _properties.update({
        'type': 'referenceresult',
        'subfields': ('uid', 'result', 'min', 'max', 'error'),
        'subfield_labels': {'uid': _('Analysis Service'),
                           'result': _('Expected Result'),
                           'error': _('Permitted Error %'),
                           'min': _('Min'),
                           'max': _('Max')},
        })
    security = ClassSecurityInfo()

registerField(ReferenceResultsField,
              title="Reference Values",
              description="Used for storing reference results",
              )
