from django.apps import AppConfig


class GparserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gparser"

    def ready(self):
        from gparser import updater
        updater.start()
