# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales/Purchase barcode',
    'summary':"""This module add the barcode in the sales/purchases lines""",
    'version': '14.0.0.1.0',
    'author':'SARL FOCUS SYSTEM.',
    'maintainer': 'SARL FOCUS SYSTEM.',
    'contributors':['contact <contact@focussystem.dz>'],
    'website':'http://www.focussystem.dz',
    'depends': ['sale_management','purchase'],
    'data': [
        'views/sale_views_inherit.xml',
        'views/purchase_views_inherit.xml',
    ],
    'license': 'AGPL-3',
    'price': 10.00,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
    'application':True,
    'images': ['static/description/poster_image.png'],
}
