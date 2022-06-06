from unittest import signals
from django.apps import AppConfig


class BorrowingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'borrowing'

    def ready(self) -> None:
        import borrowing.signals.handlers