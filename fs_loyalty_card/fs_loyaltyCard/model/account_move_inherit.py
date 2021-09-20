# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class AccountMoveFocus(models.Model):
    _inherit = 'account.move'
    @api.model
    def _get_invoice_in_payment_state(self):
    	res=super(AccountMoveFocus,self)._get_invoice_in_payment_state()
    	partner_obj=self.env['sale.order']
    	self.env.add_to_compute(partner_obj._fields['state'],partner_obj.search([]))
    	return res