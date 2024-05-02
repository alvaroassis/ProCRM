from odoo import http
from odoo.http import request


class IntranetProdemgeController(http.Controller):

    @http.route('/intranet', type='http', auth='user')
    def intranet_prodemge(self, **kwargs):
        intranet_prodemge_url = request.env['ir.config_parameter'].sudo().get_param('prodemge_intranet.intranet_prodemge_url')
        return request.render('prodemge_intranet.intranet_iframe', {'intranet_prodemge_url': intranet_prodemge_url})