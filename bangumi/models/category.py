from odoo import models, fields, api

#类别模型
class Category(models.Model):
    _name = 'bangumi.category'
    _description = 'Bangumi category'


    @api.model
    def _get_current_uid(self):
        return self.env.uid

    name = fields.Char(string='名字', required=True)
    #所有Many2one字段(多对一字段,也叫外键字段)后缀名应为_id,不成文规定
    #这里的Many2one字段关联到odoo的用户模型res.users
    #Many2one字段还有一个参数是ondelete,指明了当关联的用户删除后,当前模型应该做什么操作:set null当关联用户删除后,user_id字段设置为空, restrict限制关联的用户删除,用户删除后会提示报错, cascade
    user_id = fields.Many2one(
        'res.users', string='用户', required=True,
        default=_get_current_uid
    )

    #属性:1.反向关联的模型(bangumi.bangumi);2.当前模型在反向关联的模型中定义为哪个字段(category_id)
    bangumi_ids = fields.One2many(
        'bangumi.bangumi', 'category_id',
        string='番剧类别设置'
    )