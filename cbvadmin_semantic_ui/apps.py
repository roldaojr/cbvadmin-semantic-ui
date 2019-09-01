from django.apps import AppConfig
from cbvadmin.sites import site


class CBVAdminConfig(AppConfig):
    name = 'cbvadmin_semantic_ui'
    verbose_name = 'Semantic UI'

    def ready(self):
        super(CBVAdminConfig, self).ready()
        site.register('semantic-ui', self, 'template_pack')
