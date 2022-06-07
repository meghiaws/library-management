from django.db import transaction
from celery import shared_task

from borrowing.models import BorrowedBook
from .models import Fine


@shared_task
def create_fines():
    with transaction.atomic():
        borrowed_books = BorrowedBook.objects.select_related(
            "book_item", "borrower"
        ).all()

        for borrowed_book in borrowed_books:
            if borrowed_book.is_due_date_past():
                try:
                    # Updating exsisting fine amount if there was a fine for this borrowed_book
                    fine = Fine.objects.get(borrowed_book=borrowed_book)
                    fine.amount = Fine.calculate_fine(borrowed_book)
                    fine.save(update_fields=["amount"])

                except Fine.DoesNotExist:
                    # Createing new fine if there wasn't any fine for this borrowed_book
                    new_fine = Fine(
                        member=borrowed_book.borrower,
                        borrowed_book=borrowed_book,
                    )
                    new_fine.amount = Fine.calculate_fine(borrowed_book)
                    new_fine.save()
