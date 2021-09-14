# -*- coding: utf-8 -*-
{
    'name': 'Sale price history',
    'summary':"""This module allows you to add the sale price history""",
    'depends': ['product','sale'],
    'version': '14.0.0.1.0',
    'category': 'product',
    'author':'SARL FOCUS SYSTEM.',
    'maintainer': 'SARL FOCUS SYSTEM.',
    'contributors':['contact <contact@focussystem.dz>'],
    'website':'http://www.focussystem.dz',
    'data':[
        'views/product_template_views_inherit.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False,
    'application':True,
}
