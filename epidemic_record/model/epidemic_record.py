from odoo import api, fields, models


class EpidemicRecord(models.Model):
    _name = 'epidemic.record'
    _description = 'record'



    name = fields.Char(string='姓名')
    date = fields.Date(string='确诊日期')
    state = fields.Char(string='省')
    city = fields.Char(string='市')
    country = fields.Char(string='区/县')
    street = fields.Char(string='具体地址')
    ill_type = fields.Char(string='感染方式')
    within_or_abroad = fields.Selection([('within', '境内'),('abroad', '境外')], string='境内/境外感染')



