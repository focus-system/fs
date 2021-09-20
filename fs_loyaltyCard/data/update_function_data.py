# -*- coding: utf-8 -*-
import logging

from openerp import api, models
_logger = logging.getLogger('__name__')

class UpdateFunctionData(models.TransientModel):
    _name = "update.function.data"

    @api.model
    def update_sale_config_settings(self):
        _logger.info("===== START: UPDATE SALE CONFIG SETTINGS =====")
        # For group
        config_data = {
            'product_pricelist_setting': 'advanced',
            'group_sale_pricelist': True,
            'group_product_pricelist': False
        }
        SaleConfig = self.env['res.config.settings']
        fs = dict(SaleConfig._fields)
        vals = SaleConfig.default_get(fs)
        vals.update(config_data)
        sale_config = SaleConfig.create(vals)
        sale_config.execute()
        _logger.info("===== END: UPDATE SALE CONFIG SETTINGS =====")
        return True
