from odoo import models, fields, api

class AccountTransaction(models.Model):
    _name = 'account.transaction'
    _description = 'Accounting Transaction'
    _inherit = ['mail.thread', 'mail.activity.mixin', ] #chatter

    name = fields.Char(
        string='Transaction Number',
        required=True,
        copy=False,
        readonly=True,
        default='New',
        tracking=True, #chatter
    )
    amount = fields.Float(string='Amount', required=True, tracking=True,)
    date = fields.Date(string='Transaction Date', default=fields.Date.today, tracking=True,)
    description = fields.Text(string='Description', tracking=True,)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled')
    ], string='State', default='draft', tracking=True,)
    account_id = fields.Many2one('account.account', string='Account', tracking=True,)
    partner_id = fields.Many2one( # Relasi ke modul Contact
        comodel_name='res.partner',
        string='Contact', 
        required=True, 
        ondelete='cascade',
        tracking=True,
    )  
    # transaction_id = fields.Many2one(
    #     comodel_name='sale.order',  # Hubungkan ke model sale.order
    #     string="Sales Order",
    #     domain="[('partner_id', '=', partner_id)]",
    #     help="Reference to the related sales order.",
    # )

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('account.transaction') or '/'
        return super(AccountTransaction, self).create(vals)

    @api.model
    def default_get(self, fields):
        """ Set default partner_id to current user's contact if applicable """
        res = super(AccountTransaction, self).default_get(fields)
        user_partner = self.env.user.partner_id
        if user_partner:
            res['partner_id'] = user_partner.id
        return res
    
    # untuk penggunaan tombol statusbar
    def action_set_draft(self):
        for record in self:
            record.state = 'draft'

    def action_set_confirmed(self):
        for record in self:
            record.state = 'confirmed'

    def action_set_canceled(self):
        for record in self:
            record.state = 'canceled'

    def action_confirm(self):
        for record in self:
            previous_state = record.state
            record.state = 'confirmed'
            record.message_post(
                body=f"Status changed from <b>{previous_state}</b> to <b>Confirmed</b>",
                subtype_xmlid="mail.mt_note"
            )
            
# class SaleOrder(models.Model):
#     _inherit = 'sale.order'  # Inherit dari sale.order

#     transaction_id = fields.Many2one(
#         comodel_name='account.transaction',
#         string='Accounting Transaction',
#         domain="[('partner_id', '=', partner_id)]",  # Relasi dengan partner_id
#         help='Reference to the accounting transaction.'
#     )
# class AccountTransactionReport(models.AbstractModel):
#     _name = 'report.data_transactions.report_account_transaction'
#     _description = 'Report for Account Transactions'

#     @api.model
#     def _get_report_values(self, docids, data=None):
#         report = self.env['ir.actions.report']._get_report_from_name('data_transaction.report_name')
#         docs = self.env['account.transaction'].browse(docids)
#         return {
#             'docs': docs,
#             'data': data,
#         }
    # # report
    # def get_report_values(self, docids, data=None):
    #     docs = self.env['account.transaction'].browse(docids)
    #     return {
    #         'docs': docs,
    #         'data': data,
    #     }
