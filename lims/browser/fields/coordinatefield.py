from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import makeDisplayList
from dependencies.dependency import RecordField, RecordsField
from dependencies.dependency import registerField
from dependencies.dependency import *
from dependencies.dependency import getToolByName
from dependencies.dependency import RegexValidator
import sys
from lims import bikaMessageFactory as _
from lims.utils import t

class CoordinateField(RecordField):
    """ Stores angle in deg, min, sec, bearing """
    security = ClassSecurityInfo()
    _properties = RecordField._properties.copy()
    _properties.update({
        'type' : 'angle',
        'subfields' : ('degrees', 'minutes', 'seconds', 'bearing'),
##        'required_subfields' : ('degrees', 'minutes', 'seconds', 'bearing'),
        'subfield_labels':{'degrees':_('Degrees'),
                           'minutes':_('Minutes'),
                           'seconds':_('Seconds'),
                           'bearing':_('Bearing')},
        'subfield_sizes': {'degrees':3,
                           'minutes':2,
                           'seconds':2,
                           'bearing':1},
        'subfield_validators' : {'degrees':'coordinatevalidator',
                                 'minutes':'coordinatevalidator',
                                 'seconds':'coordinatevalidator',
                                 'bearing':'coordinatevalidator',},
        })

registerField(CoordinateField,
              title = "Coordinate",
              description = "Used for storing coordinates",
              )
