from odoo import http


class Records(http.Controller):

    @http.route('/epidemic/record', auth='user')
    def list(self, **kwargs):
        Record = http.request.env['epidemic.record']
        records = Record.search([])
        return http.request.render(
            'epidemic_record.epidemic_record_template',
            {'records': records})
