from django.apps import AppConfig


class GamesConfig(AppConfig):
    name = 'games'

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals
