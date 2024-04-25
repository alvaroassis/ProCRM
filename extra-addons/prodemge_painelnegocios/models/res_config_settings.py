# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _

# from werkzeug import urls


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    painel_negocios_url = fields.Char(
        'URL do Painel de Negócios',
        default="https://www.prodemge.gov.br",
        help="Insira a URL de acesso ao painel de indicadores de negócios",
        readonly=False, store=True)