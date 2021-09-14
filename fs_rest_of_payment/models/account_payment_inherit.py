# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Payement(models.Model):
    _inherit = "account.payment"
    Reste = fields.Monetary(string="Remaining amount",currency_field='currency_id',compute='CalculeReste')
    @api.depends('reconciled_invoice_ids')
    def CalculeReste(self):
        for rec in self:
            x=rec.amount
            y=0
            for i in rec.reconciled_invoice_ids:
                y+=rec.reconciled_invoice_ids.amount_total
            if (x-y)>=0:
                rec.Reste=x-y
            else:
                rec.Reste=0