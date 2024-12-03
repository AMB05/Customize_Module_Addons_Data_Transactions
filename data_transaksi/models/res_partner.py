from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    account_transaction_ids = fields.One2many(
        comodel_name='account.transaction',  # Model transaksi yang terkait
        inverse_name='partner_id',           # Field Many2one di model transaksi
        string='Account Transactions'
    )
    
    transaction_count = fields.Integer(  
    string='Transaction Count',  
    compute='_compute_transaction_count',  
    store=True,  
    readonly=True
    )  

    @api.depends('account_transaction_ids')  
    def _compute_transaction_count(self):  
        for partner in self:  
            partner.transaction_count = self.env['account.transaction'].search_count([('partner_id', '=', partner.id)])
            
    # Fungsi untuk menampilkan transaksi yang terkait dengan partner
    def action_account_transaction_test(self):
        self.ensure_one()  # Pastikan hanya satu record yang diproses
        return {
            'type': 'ir.actions.act_window',
            'name': 'Accounting Transactions',
            'res_model': 'account.transaction',
            'view_mode': 'tree,form',
            'domain': [('partner_id', '=', self.id)],  # Filter transaksi berdasarkan partner_id
            'context': {'default_partner_id': self.id},  # Kirim context dengan partner_id
        }

    
    