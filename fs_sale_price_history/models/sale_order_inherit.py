from odoo import api, fields, models
from datetime import date
class SaleInherit(models.Model):
    _inherit = 'sale.order.line'
    @api.onchange('price_unit')
    def insertPriceFour(self):
    	for rec in self:
    		if rec.price_unit:
    			product = self.env['product.template'].search([('id', '=', rec.product_id.id)])
    			if rec.price_unit != product.list_price and rec.price_unit > 0:
    				product.client_ids = [(0, 0, {'price':rec.price_unit,'date':date.today(),'client':rec.order_id.partner_id.id})]