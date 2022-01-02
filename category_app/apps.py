from django.apps import AppConfig


class CategoryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category_app'


class CategorySignal(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'category_app'
    def ready(self):
        from category_app.custom_signals import cat_sulg_generate_pre_save
