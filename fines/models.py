from decimal import Decimal
from django.db import models


class Fine(models.Model):
    member = models.ForeignKey("accounts.Member", on_delete=models.CASCADE)
    borrowed_book = models.OneToOneField(
        "borrowing.BorrowedBook", on_delete=models.CASCADE, unique=True
    )
    amount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    @staticmethod
    def calculate_fine(borrowed_book) -> Decimal:
        past_days_count = borrowed_book.how_many_days_past_from_due_date()
        return Decimal(past_days_count * 5.00)

    def __str__(self) -> str:
        return f"Fine: {self.amount} for {self.member}"
