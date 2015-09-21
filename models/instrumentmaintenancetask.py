# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import DateTime
# from dependencies.dependency import schemata
# from dependencies import atapi
# from dependencies.dependency import *
# from dependencies.dependency import getToolByName
# from dependencies.dependency import safe_unicode
# from lims import bikaMessageFactory as _
# from lims.utils import t
# from lims.browser.widgets import DateTimeWidget
# from lims.config import PROJECTNAME
# from lims.content.bikaschema import BikaSchema


from lims import bikaMessageFactory as _
from fields.string_field import StringField
from fields.text_field import TextField
from fields.date_time_field import DateTimeField
from fields.fixed_point_field import FixedPointField
from fields.boolean_field import BooleanField
from fields.widget.widget import StringWidget, TextAreaWidget, DateTimeWidget, BooleanWidget, ReferenceWidget, DecimalWidget
from openerp import fields, models
from models.base_olims_model import BaseOLiMSModel

#schema = BikaSchema.copy() + Schema((
schema = (


        fields.Many2one(string='Instrument',
                   comodel_name='olims.instrument',
  #     allowed_types=('Instrument',),
  #       relationship='InstrumentMaintenanceTaskInstrument',
  #       widget=StringWidget(
  #           visible=False,
  #       )

    ),

    # ComputedField('InstrumentUID',
    #     expression = 'context.getInstrument() and context.getInstrument().UID() or None',
    #     widget=ComputedWidget(
    #         visible=False,
    #     ),
    # ),

    StringField('Type',
        vocabulary = "getMaintenanceTypes",
        widget = ReferenceWidget(
            checkbox_bound = 0,
            label = _("Maintenance type",
                      "Type"),
        ),
    ),

    DateTimeField('DownFrom',
        with_time = 1,
        with_date = 1,
        required = 1,
        widget = DateTimeWidget(
            label=_("From"),
            description=_("Date from which the instrument is under maintenance"),
            show_hm = True,
        ),
    ),

    DateTimeField('DownTo',
        with_time = 1,
        with_date = 1,
        widget = DateTimeWidget(
            label=_("To"),
            description=_("Date until the instrument will not be available"),
            show_hm = True,
        ),
    ),

    StringField('Maintainer',
        widget = StringWidget(
            label=_("Maintainer"),
            description=_("The analyst or agent responsible of the maintenance"),
        )
    ),

    TextField('Considerations',
        default_content_type = 'text/plain',
        allowed_content_types= ('text/plain', ),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            label=_("Considerations"),
            description=_("Remarks to take into account for maintenance process"),
        ),
    ),

    TextField('WorkPerformed',
        default_content_type = 'text/plain',
        allowed_content_types= ('text/plain', ),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            label=_("Work Performed"),
            description=_("Description of the actions made during the maintenance process"),
        ),
    ),

    TextField('Remarks',
        default_content_type = 'text/plain',
        allowed_content_types= ('text/plain', ),
        default_output_type="text/plain",
        widget = TextAreaWidget(
            label=_("Remarks"),
        ),
    ),

    FixedPointField('Cost',
        default = '0.00',
        widget = DecimalWidget(
            label=_("Price"),
        ),
    ),

    BooleanField('Closed',
        default = '0',
        widget = BooleanWidget(
            label=_("Closed"),
            description=_("Set the maintenance task as closed.")
        ),
    ),
)

# IdField = schema['id']
# schema['description'].required = False
# schema['description'].widget.visible = True
# schema['description'].schemata = 'default'
#
# # Title is not needed to be unique
# schema['title'].validators = ()
# schema['title']._validationLayer()

class InstrumentMaintenanceTaskStatuses:
    CLOSED = 'Closed'
    CANCELLED = 'Cancelled'
    OVERDUE = "Overdue"
    PENDING = "Pending"
    INQUEUE = "In queue"

class InstrumentMaintenanceTask(models.Model, BaseOLiMSModel): #BaseFolder
    _name = 'olims.instrument_maintenance_task'
    # security = ClassSecurityInfo()
    # schema = schema
    # displayContentsTab = False

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    def getMaintenanceTypes(self):
        """ Return the current list of maintenance types
        """
        types = [('Preventive',safe_unicode(_('Preventive')).encode('utf-8')),
                 ('Repair', safe_unicode(_('Repair')).encode('utf-8')),
                 ('Enhancement', safe_unicode(_('Enhancement')).encode('utf-8'))]
        return DisplayList(types)

    def getCurrentStateI18n(self):
        return safe_unicode(_(self.getCurrentState()).encode('utf-8'))

    def getCurrentState(self):
        workflow = getToolByName(self, 'portal_workflow')
        if self.getClosed():
            return InstrumentMaintenanceTaskStatuses.CLOSED
        elif workflow.getInfoFor(self, 'cancellation_state', '') == 'cancelled':
            return InstrumentMaintenanceTaskStatuses.CANCELLED
        else:
            now = DateTime()
            dfrom = self.getDownFrom()
            dto = self.getDownTo() and self.getDownTo() or DateTime(9999, 12, 31)
            if (now > dto):
                return InstrumentMaintenanceTaskStatuses.OVERDUE
            if (now >= dfrom):
                return InstrumentMaintenanceTaskStatuses.PENDING
            else:
                return InstrumentMaintenanceTaskStatuses.INQUEUE

#atapi.registerType(InstrumentMaintenanceTask, PROJECTNAME)
InstrumentMaintenanceTask.initialze(schema)