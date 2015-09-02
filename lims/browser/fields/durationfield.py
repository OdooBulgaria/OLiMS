from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import RecordField
from dependencies.dependency import registerField
from dependencies.dependency import *
from lims import bikaMessageFactory as _
from lims.utils import t


class DurationField(RecordField):

    """ Stores duration in Days/Hours/Minutes """
    security = ClassSecurityInfo()
    _properties = RecordField._properties.copy()
    _properties.update({
        'type': 'duration',
        'subfields': ('days', 'hours', 'minutes'),
        'subfield_labels': {'days': _('Days'),
                            'hours': _('Hours'),
                            'minutes': _('Minutes')},
        'subfield_sizes': {'days': 2,
                           'hours': 2,
                           'minutes': 2},
        'subfield_validators': {'days': 'duration_validator',
                                'hours': 'duration_validator',
                                'minutes': 'duration_validator'},
    })

registerField(DurationField,
              title="Duration",
              description="Used for storing durations",
              )
