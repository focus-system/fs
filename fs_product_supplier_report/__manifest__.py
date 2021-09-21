# -*- coding: utf-8 -*-
{
    'name': 'Product supplier report',    
    'summary':"""This module displays a list that summarizes the purchases of each supplier by product""",
    'depends': ['product','purchase','stock'],
    'version': '14.0.0.1.0',
    'author':'SARL FOCUS SYSTEM.',
    'maintainer': 'SARL FOCUS SYSTEM.',
    'contributors':['contact <contact@focussystem.dz>'],
    'website': 'http://www.focussystem.dz',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/porduct_supplier_view.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
