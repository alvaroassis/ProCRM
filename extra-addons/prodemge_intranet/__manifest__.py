{
    'name': "Intranet Prodemge",
    'version': '1.0',
    'category': 'Tools/UI',
    'summary': """Módulo de Acesso a Intranet""",
    'description': """Módulo que habilita o acesso a Intranet 
    Prodemge.""",
    'author': 'Alvaro de Assis Silveira',
    'company': 'Prodemge',
    'maintainer': 'Prodemge',
    'website': 'https://prodemge.gov.br',
    'depends': ['base'],
    'data': [
    #     'security/ir.model.access.csv',
        'security/res_groups.xml',
        'views/res_config_settings_views.xml',
        'templates/intranet.xml',
        'views/intranetprodemge_load.xml',
        'views/intranetprodemge_menu.xml',

    ],
    'assets': {
        'web.assets_backend': [
           'prodemge_intranet/static/src/scss/hide_header.css',

        ],
    },

    'license': "AGPL-3",
    'installable': True,
    'auto_install': True,
    'application': True,
}