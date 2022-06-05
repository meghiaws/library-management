from datetime import date
from django.db import models
from django.core.validators import MinValueValidator


class BorrowedBook(models.Model):
    book_item = models.OneToOneField("library.BookItem", on_delete=models.CASCADE)
    borrower = models.OneToOneField("accounts.Member", on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(validators=[MinValueValidator(date.today)])

    def __str__(self):
        return (
            f"{self.book_item.book.title} borrowed from {self.borrower.user.username}"
        )
