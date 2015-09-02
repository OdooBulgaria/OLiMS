# -*- coding: utf-8 -*-
{
    'name': "OLiMS",

    'summary': """Open Source LIMS""",

    'description': """
        OLiMS Modules:
            - Analysis management
            - Sampling management
    """,

    'author': "Lablynx Inc.",
    'website': "http://www.lablynx.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'demo.xml',
        'views/olims.xml',
        'views/partner.xml',
        'views/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}