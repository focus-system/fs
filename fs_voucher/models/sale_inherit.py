# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

                      

class SaleOrder(models.Model):
    _inherit = "sale.order"
    BonCommande=fields.Boolean(string="Is a voucher")
    NumBonCom = fields.Char(string="No. voucher")
    invoice_paid = fields.Char(compute='checkInvoicepaid',store=True)

    @api.depends('invoice_paid','NumBonCom','BonCommande')
    def checkInvoicepaid(self):
    	for rec in self:
    		x=rec._get_invoice_payment_state()
    		rec.invoice_paid=x

    def _get_invoice_payment_state(self):
        for rec in self:
            if rec.BonCommande:
                invoice_search_tmp = self.env['account.move'].search([('invoice_origin', '=', rec.name)],order='id asc',limit=1)
                if invoice_search_tmp.payment_state=='paid':
                    #verifie si un bon d'achat avec ce num existe deja
                    payment_search = rec.env['account.payment'].search([('partner_id', '=', rec.partner_id.id),('ref', '=', "Voucher No. "+str(rec.NumBonCom))])
                    if len(payment_search)==0:
                        invoice=self.env['account.payment'].create({
                            'partner_id':rec.partner_id.id,
                            'ref':"Voucher No. "+str(rec.NumBonCom),
                            'amount':rec.amount_untaxed,
                            })
                        action={
                        'type':'ir.actions.act_window',
                        'res_model':'account.payment',
                        'views':[(self.env.ref('account.view_account_payment_form').id,'form')]
                        }
                        payment_draft = rec.env['account.payment'].search([('partner_id', '=', rec.partner_id.id),('ref', '=', "Voucher No. "+str(rec.NumBonCom))],order='id desc')
                        payment_draft[0].state='posted'
                    return False
                else:
                    return invoice_search_tmp.payment_state
            else:
                return False

class AccountMoveFocus(models.Model):
    _inherit = 'account.move'
    @api.model
    def _get_invoice_in_payment_state(self):
        res=super(AccountMoveFocus,self)._get_invoice_in_payment_state()
        partner_obj=self.env['sale.order']
        self.env.add_to_compute(partner_obj._fields['invoice_paid'],partner_obj.search([]))
        return res