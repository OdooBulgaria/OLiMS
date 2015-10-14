# ~~~~~~~~~~ Irrelevant code for Odoo ~~~~~~~~~~~
# from dependencies.dependency import ClassSecurityInfo
# from dependencies.dependency import aq_base, aq_inner
# from dependencies.dependency import RecordsField
# from dependencies.dependency import *
# from dependencies.dependency import HoldingReference
# from dependencies.dependency import getToolByName
# from lims.browser.widgets import ServicesWidget
# from lims.browser.widgets import WorksheetTemplateLayoutWidget
# from lims.config import ANALYSIS_TYPES, PROJECTNAME
# from lims.content.bikaschema import BikaSchema
# from lims import PMF, bikaMessageFactory as _
# from dependencies.dependency import implements
# import sys


from openerp import fields, models
from lims import PMF, bikaMessageFactory as _
from models.base_olims_model import BaseOLiMSModel
#schema = BikaSchema.copy() + Schema((
schema =   (
# ~~~~~~~ To be implemented ~~~~~~~
        # RecordsField('Layout',
        # schemata = 'Layout',
        # required = 1,
        # type = 'templateposition',
        # subfields = ('pos', 'type', 'blank_ref', 'control_ref', 'dup'),
        # required_subfields = ('pos', 'type'),
        # subfield_labels = {'pos': _('Position'),
        #                    'type': _('Analysis Type'),
        #                    'blank_ref': _('Reference'),
        #                    'control_ref': _('Reference'),
        #                    'dup': _('Duplicate Of')},
        # widget = WorksheetTemplateLayoutWidget(
        #     label=_("Worksheet Layout"),
        #     description =_(
        #         "Specify the size of the Worksheet, e.g. corresponding to a "
        #         "specific instrument's tray size. Then select an Analysis 'type' "
        #         "per Worksheet position. Where QC samples are selected, also select "
        #         "which Reference Sample should be used. If a duplicate analysis is "
        #         "selected, indicate which sample position it should be a duplicate of"),
        # )
    #),
        fields.Many2one(string='Service',
                    comodel_name='olims.analysis_service',
                    required=True,
                    help='Select which Analyses should be included on the Worksheet',
#         schemata = 'Analyses',
#         required = 1,
#         multiValued = 1,
#         allowed_types = ('AnalysisService',),
#         relationship = 'WorksheetTemplateAnalysisService',
#         referenceClass = HoldingReference,
#         widget = ServicesWidget(
#             label=_("Analysis Service"),
#             description=_("Select which Analyses should be included on the Worksheet"),
#         )
    ),

        fields.Many2one(string='Instrument',
                    comodel_name='olims.instrument',
        required = False,
        help='Select the preferred instrument'
#             #     schemata = "Description",
    #     required = 0,
    #     vocabulary_display_path_bound = sys.maxint,
    #     vocabulary = 'getInstruments',
    #     allowed_types = ('Instrument',),
    #     relationship = 'WorksheetTemplateInstrument',
    #     referenceClass = HoldingReference,
    #     widget = ReferenceWidget(
    #         checkbox_bound = 0,
    #         label=_("Instrument"),
    #         description=_("Select the preferred instrument"),
    #     ),
    ),

# ~~~~~~~ To be implemented ~~~~~~~
    # ComputedField('InstrumentTitle',
    #     expression = "context.getInstrument() and context.getInstrument().Title() or ''",
    #     widget = ComputedWidget(
    #         visible = False,
    #     ),
    # ),
)

# schema['title'].schemata = 'Description'
# schema['title'].widget.visible = True
#
# schema['description'].schemata = 'Description'
# schema['description'].widget.visible = True


class WorksheetTemplate(models.Model, BaseOLiMSModel): #BaseContent
    _name = 'olims.worksheet_template'
    # security = ClassSecurityInfo()
    # displayContentsTab = False
    # schema = schema

    _at_rename_after_creation = True
    def _renameAfterCreation(self, check_auto_id=False):
        from lims.idserver import renameAfterCreation
        renameAfterCreation(self)

    #security.declarePublic('getAnalysisTypes')
    def getAnalysisTypes(self):
        """ return Analysis type displaylist """
        return ANALYSIS_TYPES

    def getInstruments(self):
        bsc = getToolByName(self, 'bika_setup_catalog')
        items = [('', '')] + [(o.UID, o.Title) for o in
                               bsc(portal_type = 'Instrument',
                                   inactive_state = 'active')]
        o = self.getInstrument()
        if o and o.UID() not in [i[0] for i in items]:
            items.append((o.UID(), o.Title()))
        items.sort(lambda x, y: cmp(x[1], y[1]))
        return DisplayList(list(items))

#registerType(WorksheetTemplate, PROJECTNAME)
WorksheetTemplate.initialze(schema)
