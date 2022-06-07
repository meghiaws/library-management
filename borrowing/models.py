from datetime import date
from django.db import models
from django.core.validators import MinValueValidator


class BorrowedBook(models.Model):
    book_item = models.OneToOneField("library.BookItem", on_delete=models.CASCADE)
    borrower = models.ForeignKey("accounts.Member", on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(validators=[MinValueValidator(date.today)])

    def is_due_date_past(self):
        if self.due_date < date.today():
            return True
        return False

    def how_many_days_past_from_due_date(self):
        td = date.today() - self.due_date
        if td.days >= 0:
            return td.days

    def __str__(self):
        return (
            f"{self.book_item.book.title} borrowed from {self.borrower.user.username}"
        )
