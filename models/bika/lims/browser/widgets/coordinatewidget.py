from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import RecordWidget
from dependencies.dependency import registerWidget
import datetime

class CoordinateWidget(RecordWidget):
    security = ClassSecurityInfo()
    _properties = RecordWidget._properties.copy()
    _properties.update({
        'macro': "bika_widgets/coordinatewidget",
    })

registerWidget(CoordinateWidget,
               title = 'CoordinateWidget',
               description = '',
               )
