from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class Librarian(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    staff_code = models.CharField(max_length=8)

    def __str__(self):
        return f"Librarian: {self.user.username}"


class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership_code = models.CharField(max_length=8)

    def __str__(self):
        return f"Member: {self.user.username}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Author: {self.name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ManyToManyField(Author)
    subject = models.CharField(max_length=127)
    page_counts = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Book: {self.title}"


class BookItem(models.Model):
    STATUS_AVAILABLE = "A"
    STATUS_BORROW = "B"
    STATUS_RESERVED = "R"
    STATUS_LOST = "L"

    STATUS_CHOICES = (
        (STATUS_AVAILABLE, "Available"),
        (STATUS_BORROW, "Borrow"),
        (STATUS_RESERVED, "Reserved"),
        (STATUS_LOST, "Lost"),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    publication_date = models.DateField()

    def __str__(self):
        return f"BookItem: {self.book.title}"


class BorrowedBook(models.Model):
    book_item = models.OneToOneField(BookItem, on_delete=models.CASCADE)
    borrower = models.OneToOneField(Member, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(validators=[MinValueValidator(date.today)])

    def __str__(self):
        return (
            f"{self.book_item.book.title} borrowed from {self.borrower.user.username}"
        )
