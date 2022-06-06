from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from library.models import BookItem

from ..models import ReservedBook


@receiver(post_save, sender=ReservedBook)
def update_status_of_book_item_to_reserved(sender, instance, created, **kwargs):
    if created:
        book_item = instance.book_item
        if book_item.is_available():
            book_item.change_status(to=BookItem.STATUS_RESERVED)


@receiver(post_delete, sender=ReservedBook)
def update_status_of_book_item_to_available(sender, instance, **kwargs):
    book_item = instance.book_item
    book_item.change_status(to=BookItem.STATUS_AVAILABLE)
