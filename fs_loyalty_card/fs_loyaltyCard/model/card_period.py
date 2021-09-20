# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
import calendar
from openerp import api, fields, models
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF

PERIOD = [('mois', 'Mois'), ('annee', 'Année(s)')]


class CardPeriod(models.Model):
    _name = 'card.period'
    _description = 'Loyalty Card Period'
    _order = 'period,nb'

    name = fields.Char(
        string='Période',
        compute='_get_period_name',
        store=1)
    nb = fields.Integer(
        string='Nombre de Mois/Années',
        required=1)
    period = fields.Selection(
        PERIOD,
        string='Période',
        required=1)

    @api.depends('nb', 'period')
    def _get_period_name(self):
        period = dict(PERIOD)
        for record in self:
            record.name = '{} {}'.format(record.nb, period.get(record.period))

    def get_period_end_date(self, start_d=None):
        def add_months(sourcedate, months):
            month = sourcedate.month - 1 + months
            year = int(sourcedate.year + month / 12 )
            month = month % 12 + 1
            day = min(sourcedate.day, calendar.monthrange(year, month)[1])
            return date(year, month, day)

        self.ensure_one()
        if not start_d:
            start_d = fields.Date.context_today(self)
        start_d = datetime.strptime(str(start_d), DF)
        mon = self.nb
        if self.period == 'year':
            mon *= 12
        end_date = add_months(start_d, mon)
        return end_date
