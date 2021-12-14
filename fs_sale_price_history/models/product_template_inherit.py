from odoo import api, fields, models
class ProductCodeFour(models.Model):
    _inherit = 'product.template'
    client_ids = fields.One2many('client.pricelist.line','product_id')

class ProductTemplateVenteline(models.Model):
    _name='client.pricelist.line'
    product_id=fields.Many2one('product.template','Product Template', index=True, ondelete='cascade')
    price = fields.Float('Price', default=0.0, digits='Product Price',required=True, help="The price to purchase a product")
    currency_id = fields.Many2one('res.currency', 'Currency',default=lambda self: self.env.company.currency_id.id,required=True)
    date = fields.Date('Date', help="Date for this client price")
    client = fields.Many2one('res.partner','Client')