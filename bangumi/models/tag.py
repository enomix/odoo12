from odoo import models, fields, api


class Tag(models.Model):
    _name = 'bangumi.tag'
    _description = 'Bangumi tag'

    name = fields.Char(string='Name', required=True)
    #用Tag给Bangumi打标签,用Many2one字段,关联res.users模型
    user_id = fields.Many2one(
        'res.users', string='User',required=True,
        default=lambda self: self.env.uid
    )

    # Many2many主要由以下几个属性组成：
    # 1.目标模型:
    # 建立多对多关系的目标模型。
    # 2.多对多关系名称:
    # 与目标模型建立的多对多关系名称，这个名称会在数据库中生成对应的表，所以命名时要注意以模块名称 + _下划线开头。
    # 3.关系中自身代表的字段:
    # 这个字段名称会在关系数据表中生成，代表当前模型数据的id。
    # 4.关系中代表目标的字段:
    # 这个字段名称会在关系数据表中生成，代表目标模型数据的id。

    # Bangumi(番剧)和Tag(标签)是多对多的关系,所以分别在Tag和Bangumi模型中都加上Many2many字段
    bangumi_ids = fields.Many2many(
        'bangumi.bangumi', 'bangumi_bangumi_tag_rel',
        'tag_id', 'bangumi_id',
        string='番剧标签设置'
    )

