{
    'name': "Painel de Negócios Prodemge",
    'version': '1.0',
    'category': 'Tools/UI',
    'summary': """Módulo de Acesso a Painel de BI""",
    'description': """Módulo que habilita o acesso ao Painel de Indicadores 
    de Business Intelligence da área de negócios.""",
    'author': 'Alvaro de Assis Silveira',
    'company': 'Prodemge',
    'maintainer': 'Prodemge',
    'website': 'https://prodemge.gov.br',
    'depends': ['base'],
    'data': [
    #     'security/ir.model.access.csv',
        'security/res_groups.xml',
        'views/res_config_settings_views.xml',
        'templates/painel.xml',
        'views/painelnegocios_load.xml',
        'views/painelnegocios_menu.xml',

    ],
    'assets': {
        'web.assets_backend': [
           'prodemge_painelnegocios/static/src/scss/hide_header.css',

        ],
    },

    'license': "AGPL-3",
    'installable': True,
    'auto_install': True,
    'application': True,
}