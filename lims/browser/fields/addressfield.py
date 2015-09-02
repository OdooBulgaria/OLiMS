from dependencies.dependency import registerField
from dependencies.dependency import RecordField


class AddressField(RecordField):
    """ dedicated address field"""
    _properties = RecordField._properties.copy()
    _properties.update({
        'type': 'address',
        'subfields': ('address', 'city', 'zip', 'state', 'district', 'country'),
        'outerJoin': '<br />',
    })


registerField(AddressField,
              title="Address",
              description="Used for storing address information",
)

