{
    'name': 'Data Transaksi',
    'version': '6.5.2',
    'category': 'Accounting',
    'summary': 'Custom Accounting Module Example',
    'author': 'AMB',
    'website': 'https://www.doodex.net/',
    'depends': ['sale','base','account','contacts',],  # Menambahkan dependensi ke modul 'account' 'contacts' 'sale'
    'data': [
        'data/sequences.xml',
        'views/account_transaction_views.xml',  # Tampilan kustom untuk modul ini
        'views/contact_transaction.xml',
        'views/menuitems.xml',
        'views/sale_order_view.xml',
        # 'views/res_partner_inherit_views.xml',  # File tampilan baru
        'security/ir.rule.xml',  # File akses keamanan
        'security/ir.model.access.csv',
        # 'security/account_transaction_security.xml',
        'report/report_account_transaction.xml', 
        
    ],
    'models': [
        'models/account_transaction.py',
        'models/res_partner.py',
        'models/sale_order.py'
    ],
    'report': [
        # 'report/report_account_transaction.xml',  
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
