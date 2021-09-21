# -*- coding: utf-8 -*-
{
    'name': 'Sale price history',
    'summary':"""This module allows you to add the sale price history""",
    'depends': ['product','sale_management'],
    'version': '14.0.0.1.0',
    'author':'SARL FOCUS SYSTEM.',
    'maintainer': 'SARL FOCUS SYSTEM.',
    'contributors':['contact <contact@focussystem.dz>'],
    'website':'http://www.focussystem.dz',
    'data':[
        'views/product_template_views_inherit.xml',
        'security/ir.model.access.csv'
    ],
    'license': 'AGPL-3',
    'price': 30.00,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
    'application':True,
    'images': ['static/description/poster_image.png'],
}
