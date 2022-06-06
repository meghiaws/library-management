from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from library.models import BookItem

from ..models import BorrowedBook


@receiver(post_save, sender=BorrowedBook)
def update_status_of_book_item_to_borrowed(sender, instance, created, **kwargs):
    if created:
        book_item = instance.book_item
        if book_item.is_available():
            book_item.change_status(to=BookItem.STATUS_BORROWED)


@receiver(post_delete, sender=BorrowedBook)
def update_status_of_book_item_to_available(sender, instance, **kwargs):
    book_item = instance.book_item
    book_item.change_status(to=BookItem.STATUS_AVAILABLE)
