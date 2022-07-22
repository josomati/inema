{
    'name' : 'crm_ammount_total',
    'version' : '15.0.1.0',
    'summary': 'customization for inema',
    'author': "TiRecursos S.A - Lcamacho@tirecursos.com",
    'description': """
Add a field that allow you to manage dolars and colones at the same time into crm
    """,
    'category': 'crm',
    'depends' : ['base','contacts','crm','sale_management'],
    'data': [
        'views/crm_leads.xml',
    ],
    'application': False,
    'license': 'LGPL-3',}