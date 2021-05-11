# -*- coding: utf-8 -*-
{
    'name': "Bangumi",

    'summary': """
        番剧""",

    'description': """
        追番
    """,
    'depends': [],

    'author': "苏鹏",

    # for the full list
    'version': '0.1',

    'depends': ['base'],

    # 要确认好先加载什么后加载什么,不然会提示外部id找不到
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus.xml',
        'views/actions.xml'
    ],
    # 'installable': True,
    'application': True,
}
