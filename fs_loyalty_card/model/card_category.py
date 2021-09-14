# -*- coding: utf-8 -*-
##############################################################################
#
# OdooBro - odoobro.contact@gmail.com
#
##############################################################################

from openerp import api, fields, models
from openerp.tools.translate import _


class CardCategory(models.Model):
    _name = 'card.category'
    _description = 'Loyalty Card Category'
    _order = 'name'

    name = fields.Char(
        string='Nom',
        required=True)

    company_id = fields.Many2one('res.company', string='Company', 
        readonly=True, default=lambda self: self.env.company)

    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', string='Currency')

    Montant_requis = fields.Float(
        string='Montant requis',
        required=True,currency_field='currency_id')

    Gain = fields.Float(
        string='Gain',
        required=True,currency_field='currency_id')

    type_ids = fields.One2many(
        string='Types',
        comodel_name='card.type',
        inverse_name='categ_id')

    _sql_constraints = [
        ('uniq_name', "unique(name)",
         _('Name value has been existed. Please choose another !'))]
