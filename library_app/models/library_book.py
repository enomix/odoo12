from odoo import api, fields, models
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError

#由models.Model派生出的一个类
class Book(models.Model):
    #_name是模型的标识符,其定义了 Odoo 全局对该模型引用的标识符
    #仅有模型名使用点号(.) 来分割关键字，其它如模块、XML 标识符、数据表名等都使用下划线(_)。
    _name = 'library.book'
    _description = 'Book'
    _order = 'name, date_published desc'#排序

    # Text fields
    name = fields.Char(
        'Title',
        default=None,
        index=True,
        help='Book cover title',
        readonly=False,
        required=True,
        translate=False,
    )
    isbn = fields.Char('ISBN')
    book_type = fields.Selection(
        [('paper','Paperback'),
         ('hard','Hardcover'),
         ('electronic','Electronic'),
         ('other', 'Other')],
        'Type')
    notes = fields.Text('Internal Notes')
    descr = fields.Html('Description')

    # Numeric fields
    copies = fields.Integer(default=1)
    avg_rating = fields.Float('Average Rating', (3, 2))
    currency_id = fields.Many2one('res.currency')
    price = fields.Monetary('价格', 'currency_id')

    # Date fields
    date_published = fields.Date()
    last_borrow_date = fields.Datetime(
        'Last Borrowed On',
        default=lambda self: fields.Datetime.now())

    # Other fields
    active = fields.Boolean('Active?', default=True)
    image = fields.Binary('Cover')

    # Relational fields
    # 多对一Many2many关联是对其他模型中记录的引用,这里是对partner记录的一个引用
    publisher_id = fields.Many2one('res.partner', string='出版社')
    author_ids = fields.Many2many('res.partner', string='作者')

    @api.multi
    def _check_isbn(self):
        """Check one Book's ISBN"""
        self.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 13:
            ponderators = [1, 3] * 6
            total = sum(a * b for a, b in zip(digits[:12], ponderators))
            remain = total % 10
            check = 10 - remain if remain != 0 else 0
            return digits[-1] == check

    @api.multi
    def button_check_isbn(self):
        for book in self:
            if not book.isbn:
                raise Warning(
                    'Please provide an ISBN13 for %s' % book.name)
            if book.isbn and not book._check_isbn():
                raise Warning(
                    '%s is an invalid ISBN' % book.isbn)
        return True

    category_id = fields.Many2one('library.book.category', string='类别')

    publisher_country_id = fields.Many2one(
        'res.country',
        string='出版国家',
        compute='_compute_publisher_country',
        inverse='_inverse_publisher_country',
        search='_search_publisher_country',
    )

    @api.depends('publisher_id.country_id')
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id

    @api.depends('publisher_country_id')
    def _inverse_publisher_country(self):
        for book in self:
            if book.publisher_id:
                book.publisher_id.country_id = book.publisher_country_id

    def _search_publisher_country(self, operator, value):
        return [('publisher_id.country_id', operator, value)]

    publisher_country_related = fields.Many2one(
        'res.country',
        string='Publisher Country (related)',
        related='publisher_id.country_id',
    )

    #sql模型约束
    _sql_constraints = [
        ('library_book_name_date_uq',#约束唯一标识符
         'UNIQUE (name, date_published)',#约束sql语法，通过标题和出版日期是否相同来确保没有重复的图书
         'Book title and publication date must be unique.'),#消息
        ('library_book_check_date',
         'CHECK (date_published <= current_date)',#检查出版日期是否为未出版
         'Publication date must not be in the future.'),
    ]

    @api.constrains('isbn')#python约束，添加了@api.constrains装饰器，检验是否包含字段，不满足条件时就抛出异常
    def _constrain_isbn_valid(self):
        for book in self:
            if book.isbn and not book._check_isbn():
                raise ValidationError(
                    '%s is an invalid ISBN' % book.isbn)
