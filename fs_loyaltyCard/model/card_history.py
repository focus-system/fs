# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from openerp import api, fields, models
import openerp.addons.decimal_precision as dp


class CardHistory(models.Model):
    _name = 'card.history'
    _description = 'Loyalty Card History'
    _order = 'end_date DESC'

    card_id = fields.Many2one(
        string='Carte',
        comodel_name='card.card',
        ondelete='cascade',
        required=1)
    start_date = fields.Date(
        string='Date début')
    end_date = fields.Date(
        string='Date fin')
    point_in_period = fields.Float(
        string='Points/Période',
        digits=dp.get_precision('Discount'))
    total_point = fields.Float(
        string='Total des points',
        digits=dp.get_precision('Discount'))
    user_id = fields.Many2one(
        string='Responsabilité',
        ondelete='set null',
        comodel_name='res.users')
    type_id = fields.Many2one(
        string='Type',
        comodel_name='card.type',
        required=1)
