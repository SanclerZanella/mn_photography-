from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'

    def ready(self):
        """
        Overwrite ready function to connect
        the checkout signals
        """
        import portfolio.signals
