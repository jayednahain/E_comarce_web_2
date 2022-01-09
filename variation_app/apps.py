from django.apps import AppConfig


class VariationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'variation_app'
class VaritaionSignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'variation_app'

    def ready(self):
        from variation_app.Custom_signals.variation_name_pre_save import variation_pre_save