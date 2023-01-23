# -*- coding: utf-8 -*-
{
    'name': "Product Additional Information",

    'summary': """
        This module generates two fields to show date of last update of price and product. And it generates a field to show default stock location in product.""",

    'author': "SR DuBfUS",
    'website': "",

    # Categories can be used to filter modules in modules listing
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'views/product_view.xml'
    ],
    'installable' : True,
    'auto_install' : True
}
