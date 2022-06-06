from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Author: {self.name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ManyToManyField(Author, related_name="books")
    subject = models.CharField(max_length=127)
    page_counts = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Book: {self.title}"


class BookItem(models.Model):
    STATUS_AVAILABLE = "A"
    STATUS_BORROWED = "B"
    STATUS_RESERVED = "R"
    STATUS_LOST = "L"

    STATUS_CHOICES = (
        (STATUS_AVAILABLE, "Available"),
        (STATUS_BORROWED, "Borrowed"),
        (STATUS_RESERVED, "Reserved"),
        (STATUS_LOST, "Lost"),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_items")
    barcode = models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    publication_date = models.DateField()

    def is_available(self):
        return self.status == self.STATUS_AVAILABLE

    def change_status(self, to: str):
        self.status = to
        self.save(update_fields=["status"])

    def __str__(self):
        return f"BookItem: {self.book.title}"
