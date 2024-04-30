from odoo import http
from odoo.http import request


class PainelNegociosController(http.Controller):

    @http.route('/painel_negocios', type='http', auth='user')
    def painel_negocios(self, **kwargs):
        painel_negocios_url = request.env['ir.config_parameter'].sudo().get_param('prodemge_painelnegocios.painel_negocios_url')
        return request.render('prodemge_painelnegocios.painelnegocios_iframe', {'painel_negocios_url': painel_negocios_url})