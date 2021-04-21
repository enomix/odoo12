from odoo.tests.common import TransactionCase

#测试代码
class TestBook(TransactionCase):

    def setUp(self, *args, **kwargs):
        #调用了父类中的setUp代码
        result = super(TestBook, self).setUp(*args, **kwargs)
        # Prepare environment with the Admin user
        # 修改了用于测试环境的self.env为使用admin用户的新环境
        user_admin = self.env.ref('base.user_admin')
        self.env = self.env(user=user_admin)
        # Setup test data
        self.Book = self.env['library.book']
        self.book_ode = self.Book.create({
            'name': 'Odoo Development Essentials',
            'isbn': '978-1-78439-279-6'})
        return result

    def test_create(self):
        "Test Books are active by default"
        self.assertEqual(self.book_ode.active, True)

    def test_check_isbn(self):
        "Check valid ISBN"
        self.assertTrue(self.book_ode._check_isbn())
