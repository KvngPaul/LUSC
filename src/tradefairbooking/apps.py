from django.apps import AppConfig


class TradefairbookingConfig(AppConfig):
    name = 'tradefairbooking'

    def ready(self):
        import tradefairbooking.signals