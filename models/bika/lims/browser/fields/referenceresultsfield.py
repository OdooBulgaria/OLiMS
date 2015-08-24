from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import makeDisplayList
from dependencies.dependency import RecordField, RecordsField
from dependencies.dependency import registerField
from dependencies.dependency import *
from dependencies.dependency import getToolByName
from dependencies.dependency import validation
from dependencies.dependency import RegexValidator
import sys
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import t


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
