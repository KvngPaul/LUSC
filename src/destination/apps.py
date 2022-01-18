from django.apps import AppConfig


class DestinationConfig(AppConfig):
    name = 'destination'

    def ready(self):
        import destination.signals