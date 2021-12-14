# -*- coding: utf-8 -*-
{
    'name': 'Product Labels',
    'summary': 'Print custom product labels with barcode',
    'version': '14.0.0.1.0',
    'author':'SARL FOCUS SYSTEM.',
    'maintainer': 'SARL FOCUS SYSTEM.',
    'contributors':['contact <contact@focussystem.dz>'],
    'website':'http://www.focussystem.dz',
    'depends': [
        'product',
    ],
    'data': [
        'report/product_label_templates.xml',
        'report/product_label_templates_1.xml',
        'report/product_label_reports.xml',
    ],
    'license': 'AGPL-3',
    'price': 10.00,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
    'application':True,
}
