from odoo import models, fields  

class SaleOrder(models.Model):  
    _inherit = 'sale.order'  

    transaction_id = fields.Many2one(
        'account.transaction', 
        string='Data Transaction', 
        tracking=True)