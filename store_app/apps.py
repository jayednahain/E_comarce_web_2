from django.apps import AppConfig


class StoreAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store_app'


class ProductSignal(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store_app'
    def ready(self):
        from store_app.custom_singnal import product_sulg_generate_pre_save