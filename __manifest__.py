{
    'name': 'Odoo School Partner Wizard',
    'version': '15.0.0.0.1',
    'summary': """
        Odoo School.
        Example Wizard
    """,
    'category': 'Customizations',
    'author': 'grigoriykosarev@gmail.com',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['contacts'],
    'external_dependencies': {'python': [], },
    'data': [
        'wizard/create_partner_multi_wizard_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'support': 'grigoriykosarev@gmail.com',
}
