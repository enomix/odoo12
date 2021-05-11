import math

from odoo import models, fields, api


class Bangumi(models.Model):
    _name = 'bangumi.bangumi'
    _description = 'Bangumi'

    #1.api.multi装饰器,这里是显示的指明_compute_current传入的self可以为一个记录集,
    # 所以在处理时需要循环对self中的每一个记录进行处理;api.multi也是常用的三个装饰器之一,除了这个之外还有api.model api.one
    #2.api.depends装饰器:因为当前剧集是通过release_date(开播时间),update_cycle(更新周期)和total(总集数)计算而来的,所以这个函数使用了api.depends装饰器,并且写入了这三个参数
    @api.multi
    @api.depends('release_date', 'update_cycle', 'total')
    def _compute_current(self):
        for record in self:
            today = fields.Date.today()
            dt = today - record.release_date
            if dt.days < 0:
                record.current = 0
                continue

            if record.update_cycle == '周':
                current = round(dt.days / 7)
                record.current = current if current < record.total else record.total

            if record.update_cycle == '月':
                month_dt = (today.year - record.release_date.year) * 12 + (today.month - record.release_date.month)
                record.current = month_dt if month_dt < record.total else record.total

            if record.update_cycle == '季度':
                quarter_dt = (today.year - record.release_date.year) * 4 + (
                        math.ceil(today.month / 3) - math.ceil(record.release_date.month / 3))
                record.current = quarter_dt if quarter_dt < record.total else record.total


    # 分别在模型,tree视图,form视图中添加了like字段之后,
    # 再添加action_like 和 action_unlike
    @api.multi
    def action_like(self):
        return self.write({'like': True})

    @api.multi
    def action_unlike(self):
        return self.write({'like': False})

    # 名称,总集数,当前已看集数,评分字段,当前播放到第几集current
    name = fields.Char(string='名称', required=True)  # required=True该列不可为空
    cover_image = fields.Binary(string='封面', attachment=True)
    total = fields.Integer(string='总集数', required=True)
    already_seen = fields.Integer(string='当前已看集数', default=0)
    score = fields.Float(string='评分', required=True, default=0.0)
    # current字段设置了compute属性,指向了_compute_current函数
    current = fields.Integer(string='当前播放到第几集', compute='_compute_current')
    #一个like字段
    like = fields.Boolean(string='喜欢', default=False)

    # 外键关联
    category_id = fields.Many2one(
        'bangumi.category', string='类别', required=False
    )

    # Bangumi(番剧)和Tag(标签)是多对多的关系,所以分别在Tag和Bangumi模型中都加上Many2many字段
    tag_ids = fields.Many2many(
        'bangumi.tag', 'bangumi_bangumi_tag_rel',
        'bangumi_id', 'tag_id',
        string='番剧标签'
    )

    # 上映时间和更新周期
    update_cycle = fields.Selection([
        ('weekly', '周更'),
        ('monthly', '月更'),
        ('quarterly', '季更'),
    ], string='更新周期', required=True, default='weekly')

    release_date = fields.Date(string='上映时间', default=fields.Date.today(), required=True)
