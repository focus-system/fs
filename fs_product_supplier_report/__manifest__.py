# -*- coding: utf-8 -*-
{
    'name': 'Product supplier report',
    'depends': ['product','purchase'],
    'version': '14.0.0.1.0',
    'category': 'product',
    'author':'SARL FOCUS SYSTEM.',
    'maintainer': 'SARL FOCUS SYSTEM.',
    'contributors':['contact <contact@focussystem.dz>'],
    'website': 'http://www.focussystem.dz',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/porduct_supplier_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
