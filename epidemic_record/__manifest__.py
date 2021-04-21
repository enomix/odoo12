{
    # name：插件模块标题的字符串
    'name': '疫情记录',

    # description：功能描述长文件，通常为RST格式
    'description': '记录疫情感染者',

    # 作者姓名
    'author': '苏鹏',

    # depends 属性可以是一个包含所用到的模块列表。
    # Odoo 会在模块安装时自动安装这些模块，这不是强制属性，但建议使用。
    # 这里使用了内核的base模块
    'depends': ['base'],

    # 写了XML文件,需要在data里面进行声明当安装或更新时需要加载的模块
    'data': [
        # 权限相关的文件,也就是security路径下的文件,要先加载
        'security/ir.model.access.csv',
        #'security/record_security.xml',
        'views/patient_view.xml',
        #'views/record_menu.xml',
    ],
    'application': True,
    'installable': True,
}
