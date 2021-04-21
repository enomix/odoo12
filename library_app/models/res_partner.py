from odoo import fields, models
#作者端
class Partner(models.Model):
    _inherit = 'res.partner'

    published_book_ids = fields.One2many(
        'library.book', # related model，关联模型 (comodel_name关键字参数)
        'publisher_id', # fields for "this" on related model,引用该记录的模型字段 (inverse_name关键字参数)
        string='Published Books')#字段标签 (string关键字参数)

    book_ids = fields.Many2many(
        'library.book', string='Authored Books')
