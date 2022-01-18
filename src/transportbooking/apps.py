from django.apps import AppConfig


class TransportbookingConfig(AppConfig):
    name = 'transportbooking'

    def ready(self):
        import transportbooking.signals