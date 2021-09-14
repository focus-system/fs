# -*- coding: utf-8 -*-
##############################################################################
#
# OdooBro - odoobro.contact@gmail.com
#
##############################################################################

{
    'name': 'Carte de fidélité',
    'version': '14.0.0.1.0',
    'category': 'sale',
    'author':'SARL FOCUS SYSTEM.',
    'maintainer': 'SARL FOCUS SYSTEM.',
    'contributors':['contact <contact@focussystem.dz>'],
    'website': 'http://www.focussystem.dz',
    'depends': ['sale','account'],
    'data': [
        # ============================================================
        # SECURITY SETTING - GROUP - PROFILE
        # ============================================================
        # 'security/',
        'security/res_groups_data.xml',
        'security/ir_rule_data.xml',
        'security/ir.model.access.csv',

        # ============================================================
        # DATA
        # ============================================================
        # 'data/',
        'data/ir_sequence_data.xml',
        'data/card_stage_data.xml',

        # ============================================================
        # VIEWS
        # ============================================================
        'views/card_period_view.xml',
        'views/card_category_view.xml',
        'views/card_type_view.xml',
        'views/card_card_view.xml',
        'views/sale_order_view.xml',

        # ============================================================
        # WIZARDS
        #=============================================================
        ##'wizards/card_process_wizard.xml',
        ##'wizards/create_card_wizard.xml',
        ##'wizards/sale_config_settings_view.xml',

        # ============================================================
        # MENU
        # ============================================================
        'menu/card_menu.xml',

        # ============================================================
        # FUNCTION USED TO UPDATE DATA LIKE POST OBJECT
        # ============================================================
        'data/update_function_data.xml',
    ],

    'test': [],
    'demo': [],

    'installable': True,
    'active': False,
    'application': True,
}
