# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PurchaseOrderCode(models.Model):
    _inherit = 'purchase.order.line'
    x_codebarre = fields.Char('Barcode')
    @api.onchange('x_codebarre')
    def _Code_barre_product(self):
        for line in self:
            if line.x_codebarre:
                product_rec=self.env['product.product'].search([])
                for pro in product_rec:
                    if pro.barcode==line.x_codebarre:
                        line.product_id=pro.id
                        product_uom=pro.product_tmpl_id.uom_po_id
                        line.price_unit=pro.lst_price

    @api.onchange('product_id')
    def _product_Code_barre(self):
        for line in self:
            if line.product_id.id:
                product_rec=self.env['product.product'].search([])
                for pro in product_rec:
                    if line.product_id.id==pro.id:
                        line.x_codebarre=pro.barcode