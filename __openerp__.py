# -*- coding: utf-8 -*-
{
    'name': "Ean 13",

    'summary': """Design Odoo for Ean13""",

    'description': """
        Project Ean13
    """,

    'author': "IGPRO",
    'website': "http://igpro-online.com",

    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','stock','purchase'],

    # always loaded
    'data': [
        'ean13.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
