from odoo import api, fields, models


class EmployeeRecord(models.Model):
    _name = 'employee.record'

    #默认返回当前用户的id
    @api.model
    def _default_create_user_id(self):
        return self.env.uid

    name = fields.Char(string='姓名')
    sex = fields.Selection([('male', '男性'),('female', '女性')], string='性别')
    image = fields.Binary(string='照片', attachment=True)
    age = fields.Char(string='年龄')
    date = fields.Date(string='入职日期')
    state = fields.Char(string='省')
    city = fields.Char(string='市')
    country = fields.Char(string='区/县')
    street = fields.Char(string='家庭住址')

    is_working = fields.Boolean(string='是否在职', default=True)
    leaving_reason = fields.Char(string='离职原因')
    email = fields.Char(string='邮箱')
    phone_number = fields.Char(string='手机')
    position = fields.Selection([('general_manager', '总经理'),('technical_director', '技术部长'),('finance_manager', '财务主管'),('human_resource', '人事主管')],string='职位')
    #default=lambda self: self.env.uid表示默认值为获取的当前登录账户的id
    # create_user_id = fields.Many2one('res.users', string='填报人', default=lambda self: self.env.uid)
    create_user_id = fields.Many2one('res.users', default=_default_create_user_id)
    note = fields.Text(string='说明')

    fuzhu_create_user_ids = fields.Many2many('res.users', 'employee_record_res_users_rel', column1='record_id', column2='user_id', string='辅助填报人')

    active = fields.Boolean(default=True)

    @api.model
    def create(self, vals_list):
        res = super(EmployeeRecord, self).create(vals_list)
        return res



    @api.multi
    def unlink(self):
        # 伪删除
        for obj in self:
            obj.active = False

    @api.onchange('state', 'city', 'name')
    def onchange_note(self):
        self.note = '{}省{}市，员工姓名{}'.format(self.state, self.city, self.name)

    def myunlink(self):
        self.active = False

    def mysearch(self):
        users_objs = self.env['res.users'].sudo().browse([2,2])
        print('users_objs', users_objs)

    def create_or_write(self):
        users_env = self.env['res.users']
        user_id = users_env.search([('name', '=', '测试账户1')])
        # 记录集在调用write方法时，只能是一条记录，如果记录集中包含多条记录则需要遍历
        res = user_id.write({
            'login': 'ceshizhanghu@163.com'
        })


