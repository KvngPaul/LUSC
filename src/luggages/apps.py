from django.apps import AppConfig


class LuggagesConfig(AppConfig):
    name = 'luggages'

    def ready(self):
        import transportbooking.signals
