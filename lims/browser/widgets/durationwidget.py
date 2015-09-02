from dependencies.dependency import ClassSecurityInfo
from dependencies.dependency import RecordWidget
from dependencies.dependency import registerWidget
import datetime

class DurationWidget(RecordWidget):
    security = ClassSecurityInfo()
    _properties = RecordWidget._properties.copy()
    _properties.update({
        'macro': "bika_widgets/durationwidget",
    })

registerWidget(DurationWidget,
               title = 'DurationWidget',
               description = (''),
               )
