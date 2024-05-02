# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    intranet_prodemge_url = fields.Char(
        string='URL da Intranet Prodemge',
        config_parameter='prodemge_intranet.intranet_prodemge_url',
        default='https://intranet.prodemge.gov.br',
        readonly=False)
