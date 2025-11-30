{
    'name': 'ZC Undergraduate Admission',
    'version': '19.0',
    'summary': 'Undergraduate Admission Management System',
    'description': 'Manage undergraduate admissions process',
    'category': 'Education',
    'author': 'Mahmoud, Omar, Sarah, Abeer',
    'website': 'https://admissions.zewailcity.edu.eg/',
    'depends': ['base', 'portal'],
    'data': [
        'views/admission_applicant_views.xml',
        'views/education_history_views.xml',
        'views/portal_templates.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
