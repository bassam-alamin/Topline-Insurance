from django.apps import AppConfig


class VehicleConfig(AppConfig):
    name = 'vehicle'

    def ready(self):
        from . import views
        views.start()
