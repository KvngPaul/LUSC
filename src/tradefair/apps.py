from django.apps import AppConfig


class TradefairConfig(AppConfig):
    name = 'tradefair'

    def ready(self):
        import tradefair.signals