# -*- coding: utf-8 -*-
{
    'name': "check_sales",

    'summary': """
        Crear proyecto desde ventas al confirmar la venta""",

    'description': """
        Crear proyecto desde ventas con etapas por default  al confirmar.
    """,

    'author': "XMARTS",
    'email': 'desarrollo@xmarts.com',
    'website': "https://xmarts.com",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application':True,
    'installable':True,
}