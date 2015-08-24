from OLiMS.dependencies.dependency import IntegerWidget as _i
from OLiMS.dependencies.dependency import registerPropertyType
from OLiMS.dependencies.dependency import registerWidget

from OLiMS.dependencies.dependency import ClassSecurityInfo

_marker = []


class IntegerWidget(_i):
    _properties = _i._properties.copy()
    _properties.update({
        'macro': "bika_widgets/integer",
        'unit': '',
    })

    security = ClassSecurityInfo()

registerWidget(IntegerWidget,
               title='Integer',
               description=('Renders a HTML text input box which '
                            'accepts a integer value'),
               )

registerPropertyType('unit', 'string', IntegerWidget)
