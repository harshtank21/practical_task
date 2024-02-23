{
    "name": "practical Task",
    'version': '16.0.1.0.0',
    'summary': 'Invoices & Payments',
    'sequence': 10,
    'description': """
School Management 
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Accounting/Accounting',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/mail_template.xml',
        'data/ir_sequence_data.xml',
        'data/ir_cron_data.xml',
        'wizard/sale_order_wizard.xml',
        'report/sale_order_report.xml',
        'report/new_one.xml',
        'views/sale_order_views_.xml',
        'views/res_config_settings_views.xml'



    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
