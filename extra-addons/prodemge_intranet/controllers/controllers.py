from odoo import http
from odoo.http import request


class IntranetProdemgeController(http.Controller):

    @http.route('/intranet', type='http', auth='user')
    def intranet_prodemge(self, **kwargs):
        if not request.env.user.has_group('prodemge_intranet.intranet_user'):
            return "Você não tem permissão para acessar esta página."
        intranet_prodemge_url = request.env['ir.config_parameter'].sudo().get_param('prodemge_intranet.intranet_prodemge_url')
        return request.render('prodemge_intranet.intranet_iframe', {'intranet_prodemge_url': intranet_prodemge_url})