====================
CBVadmin Semantic UI
====================

Template pack for CBVadmin using Semantic UI css framework

Require following existing django packages.

- crispy-semantic-ui
- django-filter

Installing and configuring
==========================

``pip install cbvadmin-semantic-ui``

Add the following to django settings.py for automatic configuration

.. code-block:: python

    from cbvadmin_semantic_ui.settings import cbvadmin_semantic_ui_settings
    ...
    cbvadmin_semantic_ui_settings(vars())

Or do manual config

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'cbvadmin_semantic_ui',
        'semantic_ui'
    ]
    ...
    CBVADMIN_TEMPLATE_PACK': 'semantic-ui',
    CRISPY_TEMPLATE_PACK': 'semantic-ui',
    CRISPY_ALLOWED_TEMPLATE_PACKS': ('semantic-ui',)
