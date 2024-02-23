from odoo import models, fields, api


class SaleOrderLines(models.Model):
    _inherit = "sale.order.line"
    _description = "task"


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "task"

    number = fields.Char('number' , related='partner_id.phone',store=True,readonly=False)

    approvers = fields.Many2many(comodel_name="res.users", string='Approval', required=True,
                                 groups="practical_task.group_order_approval_of_car_rental" )
    state = fields.Selection(
        selection_add=[
            ("approval_requested", "Approval Requested"),
            ("approved", "Approved"),
            ('sale',)
        ])
    sale_bool = fields.Boolean(
        string="SALE"
    )
    quotations_name = fields.Char('Quotations')
    sale_name = fields.Char('Quotations')

    # @api.constrains('state')
    # def new_sequence(self):
    #     print(self.name, '----------------')
    #     if self.state == 'draft' or self.state == 'sent':
    #         self.name = self.name.replace("S", "QU")
    #     elif self.state == 'sale':
    #         self.name = self.name.replace("QU", 'S')

    @api.model
    def create(self, vals):
        res = super().create(vals)
        res.sale_name = res.name
        res.name = self.env['ir.sequence'].next_by_code('my.sequence.for.sale')
        res.quotations_name = res.name
        return res

    def write(self, values):
        res = super().write(values)
        if 'state' in values:
            if values['state'] == 'draft':
                self.name = self.quotations_name
            else:
                self.name = self.sale_name
        return res

    def action_approval_requested(self):
        self.state = 'approval_requested'
        remainder_template = self.env.ref("practical_task.email_rental_two_sale")
        remainder_template.send_mail(self.id, force_send=True, raise_exception=False)

    def action_approval(self):
        self.state = 'approved'
        self.message_post(body=f'{self.approvers.name} has provided approval for the order')

    def send_approval_reminders(self):
        store = self.search([('state', '=', 'approval_requested')])
        for rec in store:
            template = rec.env.ref("practical_task.email_rental_two_sale")
            template.send_mail(rec.id, force_send=True, raise_exception=False)
