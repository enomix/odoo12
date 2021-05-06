from odoo import http


class Books(http.Controller):

    @http.route('/employee/records', auth='user')
    def list(self, **kwargs):
        Record = http.request.env['employee.record']
        records = Record.search([])
        return http.request.render(
            'employee_record.employee_record_template',
            {'records': records})
