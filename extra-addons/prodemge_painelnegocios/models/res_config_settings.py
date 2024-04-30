# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    painel_negocios_url = fields.Char(
        string='URL do Painel de Negócios',
        config_parameter='prodemge_painelnegocios.painel_negocios_url',
        default='https://www.prodemge.gov.br',
        readonly=False)
