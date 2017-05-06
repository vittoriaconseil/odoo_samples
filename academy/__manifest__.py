# -*- coding: utf-8 -*-
{
    'name': "Academy",

    'summary': """
    """,

    'description': """
    """,

    'author': "Vittoria Conseil",
    'website': "http://www.vittoriaconseil.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sample',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','website_form','website_sale'],

    # always loaded
    'data': [
        
        'data/academy.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}