from OLiMS.dependencies.dependency import SelectionWidget as _s
from OLiMS.dependencies.dependency import registerWidget

from OLiMS.dependencies.dependency import ClassSecurityInfo

class SelectionWidget(_s):
    _properties = _s._properties.copy()
    _properties.update({
        'macro': "bika_widgets/selection",
    })

    security = ClassSecurityInfo()

registerWidget(SelectionWidget)
