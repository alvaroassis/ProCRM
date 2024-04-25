{
    'name': "Painel de Negócios Prodemge",
    'version': '0.1',
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
        'views/res_config_settings.xml',
    #     'views/dashboard_menu_view.xml',
    #     'views/dynamic_block_view.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'odoo_dynamic_dashboard/static/src/js/**/*.js',
    #         'odoo_dynamic_dashboard/static/src/scss/**/*.scss',
    #         'odoo_dynamic_dashboard/static/src/xml/**/*.xml',
    #     ],
    # },
    # 'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': True,
}