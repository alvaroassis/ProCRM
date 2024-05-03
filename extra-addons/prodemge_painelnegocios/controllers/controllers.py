from odoo import http
from odoo.http import request


class PainelNegociosController(http.Controller):

    @http.route('/painel_negocios', type='http', auth='user')
    def painel_negocios(self, **kwargs):
        if not request.env.user.has_group('prodemge_painelnegocios.painelnegocios_user'):
            return "Você não tem permissão para acessar esta página."
        painel_negocios_url = request.env['ir.config_parameter'].sudo().get_param('prodemge_painelnegocios.painel_negocios_url')
        return request.render('prodemge_painelnegocios.painelnegocios_iframe', {'painel_negocios_url': painel_negocios_url})