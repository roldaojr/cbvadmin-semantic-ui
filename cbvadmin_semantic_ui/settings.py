required_settings = {
    'CBVADMIN_TEMPLATE_PACK': 'semantic-ui',
    'CRISPY_TEMPLATE_PACK': 'semantic-ui',
    'CRISPY_ALLOWED_TEMPLATE_PACKS': ('semantic-ui',),
    'CRISPY_CLASS_CONVERTERS': {
        #'select': 'ui selection fluid dropdown'
    }
}


def update_cbvadmin_settings(settings):
    settings.update(required_settings)
    return settings
