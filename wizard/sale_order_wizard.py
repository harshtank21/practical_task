from odoo import api, fields, models


class SaleOrderWizad(models.TransientModel):
    _name = 'sale.order.wizard'

    name = fields.Many2one('res.partner', string="Customer", readonly=True)