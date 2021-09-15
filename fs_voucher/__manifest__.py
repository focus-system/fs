# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Voucher',
    'summary':"""This module allows the management of vouchers""",
    'version': '14.0.0.1.0',
    'category': 'sale',
    'author':'SARL FOCUS SYSTEM.',
    'maintainer': 'SARL FOCUS SYSTEM.',
    'contributors':['contact <contact@focussystem.dz>'],
    'website':'http://www.focussystem.dz',
    'depends': ['account', 'sale'],
    'data': [
        'views/sale_views_inherit.xml'
    ],
    'license': 'AGPL-3',
    'price': 30.00,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
    'application':True,
}
