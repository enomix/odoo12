# -*- coding: utf-8 -*-
{
    'name': "员工记录",

    'summary': """
        员工记录""",

    'description': """
        员工记录
    """,

    'author': "苏鹏",

    # for the full list
    'version': '0.1',

    # always loaded
    'data': [
        'security/employee_record_security.xml',
        'views/employee_record_view.xml',
        'security/ir.model.access.csv',
        'views/employee_record_template.xml',
        'reports/employee_report.xml',
    ],
    # 'installable': True,
    'application': True,
}
