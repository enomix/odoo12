{
    #name：插件模块标题的字符串
    'name': 'Library Management Application',

    #description：功能描述长文件，通常为RST格式
    'description': 'Library books, members and book borrowing.',

    #作者姓名
    'author': 'sp',

    #depends 属性可以是一个包含所用到的模块列表。
    # Odoo 会在模块安装时自动安装这些模块，这不是强制属性，但建议使用。
    #这里使用了内核的base模块
    'depends': ['base'],

    #写了XML文件,需要在data里面进行声明当安装或更新时需要加载的模块
    'data': [
        #权限相关的文件,也就是security路径下的文件,要先加载
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_category_view.xml',
        'views/book_list_template.xml',
    ],
    'application': True,
    'installable': True,
}
