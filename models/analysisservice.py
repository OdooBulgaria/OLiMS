'''
Created on Aug 12, 2015

@author: yasir1brahim
'''

from openerp import fields, models


""" just for removing errors """
HoldingReference = ""

    
class AnalysisService(models.Model):
    _name = "olims.analysis_service"
    
    Title = fields.Char("Title", required=True)
    
    ShortTitle = fields.Char(string= "Short title", help = "If text is entered here, it is used instead of the "
                        "title when the service is listed in column headings. "
                        "HTML formatting is allowed."
                )
                                    
    Description = fields.Text("Description", help="Used in item listings and search results.")
    
    ScientificName = fields.Boolean("Scientific name", help="If enabled, the name of the analysis will be " \
                                     "written in italics.")
    
    Unit = fields.Text("Unit",help="The measurement units for this analysis service' results, " \
                        "e.g. mg/l, ppm, dB, mV, etc.")
    
    Precision = fields.Integer("Precision as number of decimals",help="Define the number of decimals to be used for this result.")
    
    ExponentialFormatPrecision = fields.Integer("Exponential format precision", \
                                                help="Define the precision when converting values to exponent " \
                                                "notation.  The default is 7.",default=7)
 
    LowerDetectionLimit = fields.Float("Lower Detection Limit (LDL)",digits=(32, 32),default=0.0,help="The Lower Detection Limit is " \
                                       "the lowest value to which the " \
                                       "measured parameter can be " \
                                       "measured using the specified " \
                                       "testing methodology. Results " \
                                       "entered which are less than " \
                                       "this value will be reported " \
                                       "as < LDL")
    
    # LIMS-1775 Allow to select LDL or UDL defaults in results with readonly mode
    # https://jira.bikalabs.com/browse/LIMS-1775
    # Some behavior controlled with javascript: If checked, the field
    # "AllowManualDetectionLimit" will be displayed.
    # See browser/js/bika.lims.analysisservice.edit.js
    #
    # Use cases:
    # a) If "DetectionLimitSelector" is enabled and
    # "AllowManualDetectionLimit" is enabled too, then:
    # the analyst will be able to select an '>', '<' operand from the
    # selection list and also set the LD manually.
    #
    # b) If "DetectionLimitSelector" is enabled and
    # "AllowManualDetectionLimit" is unchecked, the analyst will be
    # able to select an operator from the selection list, but not set
    # the LD manually: the default LD will be displayed in the result
    # field as usuall, but in read-only mode.
    #
    # c) If "DetectionLimitSelector" is disabled, no LD selector will be
    # displayed in the results table.
    
    UpperDetectionLimit = fields.Float("Upper Detection Limit (UDL)",digits=(32, 32),default=1000000000.0, \
                                       help="The Upper Detection Limit is the " \
                                       "highest value to which the " \
                                       "measured parameter can be measured " \
                                       "using the specified testing " \
                                       "methodology. Results entered " \
                                       "which are greater than this value " \
                                       "will be reported as > UDL")
    
    # Behavior controlled with javascript: Only visible when the
    # "DetectionLimitSelector" is checked
    # See browser/js/bika.lims.analysisservice.edit.js
    # Check inline comment for "DetecionLimitSelector" field for
    # further information.

    DetectionLimitSelector = fields.Boolean("Display a Detection Limit selector", \
                                             help="If checked, a selection list will be " \
                                             "displayed next to the analysis' result " \
                                             "field in results entry views. By using " \
                                             "this selector, the analyst will be able " \
                                             "to set the value as a Detection Limit " \
                                             "(LDL or UDL) instead of a regular result")

    AllowManualDetectionLimit = fields.Boolean("Allow Manual Detection Limit input", \
                                 help="Allow the analyst to manually " \
                                 "replace the default Detection Limits " \
                                 "(LDL and UDL) on results entry views")
    
    ReportDryMatter = fields.Boolean("Report as Dry Matter", \
                                      help="These results can be reported as dry matter")
    
    AttachmentOption = fields.Selection((('r', 'Required'),('p', 'Permitted'),('n', 'Not Permitted')), "Attachment Option")
    
    Keyword = fields.Char( required=False, string = "Analysis Keyword",
                    help = "The unique keyword used to identify the analysis service in "
                        "import files of bulk AR requests and results imports from instruments. "
                        "It is also used to identify dependent analysis services in user "
                        "defined results calculations",
                )

    # Allow/Disallow manual entry of results
    # Behavior controlled by javascript depending on Instruments field:
    # - If InstrumentEntry not checked, set checked and readonly
    # - If InstrumentEntry checked, set as not readonly
    # See browser/js/bika.lims.analysisservice.edit.js
    
    ManualEntryOfResults =  fields.Boolean( default=True, string = "Allow manual entry of results",
            help = "Select if the results for this Analysis Service can be set manually.",
    )

    # Allow/Disallow instrument entry of results
    # Behavior controlled by javascript depending on Instruments field:
    # - If no instruments available, hide and uncheck
    # - If at least one instrument selected, checked, but not readonly
    # See browser/js/bika.lims.analysisservice.edit.js
    InstrumentEntryOfResults = fields.Boolean (string = "Allow instrument entry of results",
        help ="Select if the results for this Analysis Service can be set using an Instrument.")
        
    # Instruments associated to the AS
    # List of instruments capable to perform the Analysis Service. The
    # Instruments selected here are displayed in the Analysis Request
    # Add view, closer to this Analysis Service if selected.
    # - If InstrumentEntry not checked, hide and unset
    # - If InstrumentEntry checked, set the first selected and show
   
    
def model_fields_gen(self, field_tuples):
    
    pass


