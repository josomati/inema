{
    'name' : 'Tir_crm_ammount_total',
    'version' : '15.0.1.0',
    'summary': '',
    'sequence': 1,
    'description': """
Add a field that allow you to manage dolars and colones at the same time into crm
    """,
    'category': 'crm',
    'depends' : ['base','contacts','crm','sale_management'],
    'data': [
        'views/crm_leads.xml',
    ],
    'application': True,
    'license': 'LGPL-3',}