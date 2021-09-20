# -*- coding: utf-8 -*-

from openerp import api, fields, models
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(compute="_update_loyalty_point",store=True)
    paid_invoice = fields.Boolean(default=False,store=True)
    upgrade_message = fields.Char(
        string="Message Box",
        compute="_get_needed_amount_msg",
        store=True)
    card_id = fields.Many2one(
        string='Loyalty Card',
        comodel_name='card.card',
        inverse='_dump_func',
        search='_search_by_card',
        compute='_dump_func')

    #@api.multi (delete)
    def _dump_func(self):
        pass

    #@api.multi (delete)
    def _search_by_card(self, operator, value):
        partner_ids = []
        if value:
            args = [('partner_id', '!=', False)]
            cards = self.env['card.card'].name_search(value, args)
            if cards:
                card_ids = [x[0] for x in cards]
                cards = self.env['card.card'].browse(card_ids)
                partner_ids = [x.partner_id.id for x in cards]
        return [('partner_id', 'in', partner_ids)]

    @api.onchange('card_id')
    def _set_customer(self):
        for order in self:
            if not self.card_id or not self.card_id.partner_id:
                continue
            order.partner_id = self.card_id.partner_id

    def _update_loyalty_point(self):
        for order in self:
            if not order.paid_invoice:
                if order.state != 'sale':
                    continue
                card = self.env['card.card']._get_card(order.partner_id.id)
                if not card:
                    continue  
                invoice_search_tmp = self.env['account.move'].search([('invoice_origin', '=', order.name)],order='id asc',limit=1)
                if invoice_search_tmp.payment_state!='paid':
                    continue
                points = card.convert_amount_to_point(order.amount_total)
                card.resteAmount=card.resteAmount+(order.amount_total-(points*card.type_id.categ_id.Montant_requis))
                pointsReste=0
                if card.resteAmount >= card.type_id.categ_id.Montant_requis :
                    pointsReste = card.convert_amount_to_point(card.resteAmount)
                    card.resteAmount=card.resteAmount-(pointsReste*card.type_id.categ_id.Montant_requis)
                    points +=pointsReste
                card.total_point += points
                card.point_in_period += points
                payment_search = order.env['account.payment'].search([('partner_id', '=', order.partner_id.id),('ref', '=', 'Carte de fidélité')],order='id desc')
                if not payment_search:
                    invoice=self.env['account.payment'].create({
                        'partner_id':order.partner_id.id,
                        'ref':'Carte de fidélité',
                        'amount':points*card.type_id.categ_id.Gain,
                        })
                    action={
                    'type':'ir.actions.act_window',
                    'res_model':'account.payment',
                    'views':[(self.env.ref('account.view_account_payment_form').id,'form')]
                    }    
                    payment_posted = order.env['account.payment'].search([('partner_id', '=', order.partner_id.id),('ref', '=', 'Carte de fidélité')],order='id desc')
                    payment_posted[0].state='posted'
                elif payment_search:
                    if payment_search[0].reconciled_invoices_count!=0:
                        invoice=self.env['account.payment'].create({
                            'partner_id':order.partner_id.id,
                            'ref':'Carte de fidélité',
                            'amount':points*card.type_id.categ_id.Gain,
                            })
                        action={
                        'type':'ir.actions.act_window',
                        'res_model':'account.payment',
                        'views':[(self.env.ref('account.view_account_payment_form').id,'form')]
                        } 
                        payment_posted = order.env['account.payment'].search([('partner_id', '=', order.partner_id.id),('ref', '=', 'Carte de fidélité')],order='id desc')
                        payment_posted[0].state='posted'
                    else:
                        payment_search[0].amount+=points*card.type_id.categ_id.Gain
                order.paid_invoice=True


    @api.depends('order_line', 'state')
    def _get_needed_amount_msg(self):
        for order in self:
            msg = u''
            if order.state != 'draft':
                order.upgrade_message = msg
                continue
            card = self.env['card.card']._get_valid_card(order.partner_id.id)
            if not card:
                order.upgrade_message = msg
                continue
            remind_rate = order.company_id.lc_remind_point_rate
            if not remind_rate:
                order.upgrade_message = msg
                continue
            type = card.type_id._get_next_type()
            if type:
                amount_in_period = \
                    card.convert_point_to_amount(card.point_in_period)
                amount_onhand = order.amount_total + amount_in_period
                basic_amount = card.convert_point_to_amount(type.basic_point)
                if basic_amount > amount_onhand:
                    prate = round(float(amount_onhand)/float(basic_amount),2)
                    if prate >= remind_rate:
                        needed_amount = basic_amount - amount_onhand
                        msg = _(u'''Need more {:,} to upgrade the customer card
                        with the new discount {}%
                        '''.format(needed_amount, type.discount))
                else:
                    msg = _(u'''After done this order, this customer is
                    eligible to upgrade his/her loyalty card {}
                    with the new discount {}%.
                    '''.format(card.name, type.discount))            
            order.upgrade_message = msg

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super(SaleOrder, self).onchange_partner_id()
        card = self.env['card.card']._get_valid_card(self.partner_id.id)
        if card and card.pricelist_id:
            self.pricelist_id = card.pricelist_id.id
