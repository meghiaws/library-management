from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class ReservedBook(models.Model):
    book_item = models.OneToOneField("library.BookItem", on_delete=models.CASCADE)
    reserver = models.ForeignKey("accounts.Member", on_delete=models.SET_NULL, null=True)
    reserved_at = models.DateTimeField(auto_now_add=True)
    due_time = models.DateTimeField(validators=[MinValueValidator(timezone.now)])

    def __str__(self):
        return (
            f"{self.id}"
        )
