from . import REQUIRED_APPS

required_settings = {
    'CBVADMIN_TEMPLATE_PACK': 'semantic-ui',
    'CRISPY_TEMPLATE_PACK': 'semantic-ui',
    'CRISPY_ALLOWED_TEMPLATE_PACKS': ('semantic-ui',)
}


def cbvadmin_semantic_ui_settings(settings):
    settings.update(required_settings)
    if 'INSTALLED_APPS' not in settings:
        settings['INSTALLED_APPS'] = []
    settings['INSTALLED_APPS'] += REQUIRED_APPS
    return settings
