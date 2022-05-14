from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        """
        Overwrite ready function to connect
        the checkout signals
        """
        import home.signals
