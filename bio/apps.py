from django.apps import AppConfig


class BioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bio'

    def ready(self):
        """
        Overwrite ready function to connect
        the checkout signals
        """
        import bio.signals
