{
    'name': 'partner_project',
    'version': '15.0.1.0',
    'summary': '',
    'autor': 'Ti Recursos S.A',
    'sequence': 1,
    'description': """
partner_project for inema
====================

    """,
    'category': 'Hidden/Tools',
    'depends': ['base', 'contacts'],
    'data': [
    "security/ir.model.access.csv",
    "views/partner_project.xml",
    "views/contact_views.xml"
    ],
    'application': False,
    'license': 'LGPL-3',
}
