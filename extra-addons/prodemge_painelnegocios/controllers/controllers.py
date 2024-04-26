from odoo import http

class PainelController(http.Controller):
    @http.route('/painel', type='http', auth='user')
    def painel(self):
        record = http.request.env['res.config.settings'].search([], limit=1)
        url = record.painel_negocios_url if record else ''
        return """
            <html>
                <body>
                    <iframe src="{}" width="100%" height="500"></iframe>
                </body>
            </html>
        """.format(url)