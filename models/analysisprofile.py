'''
Created on Aug 15, 2015

@author: yasir1brahim
'''

from openerp import fields, models
from openerp.tools import float_round, frozendict, html_sanitize, ustr
#, OrderedSet

class my_field(fields.Field):
    type = 'boolean'
    
    def convert_to_cache(self, value, record, validate=True):
        return bool(value)

    def convert_to_export(self, value, env):
        if env.context.get('export_raw_data'):
            return value
        return ustr(value)
    


class Analysis(models.Model):
    _name="olims.analysis_profile"
    
    
    title = fields.Char(string="Title", help="")
    
    Profile_Key = fields.Char(string="Profile Keyword", help = "The profile's keyword is used to uniquely identify " + \
            "it in import files. It has to be unique, and it may " + \
            "not be the same as any Calculation Interim field ID.")\
            
#     service = fields.many2one("Profile Analyses", help="The analyses included in this profile, grouped per category",)
    service = fields.Reference(string="Analysis Service", selection=[("olims.analysis_service", "Analysis Service")])
    
    field_dummy = my_field(string="Field Dummy")

