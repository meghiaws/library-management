from django.contrib import admin
from .models import Author, Book, BookItem


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "isbn",
        "subject",
        "page_counts",
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
    )

@admin.register(BookItem)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book_id",
        "barcode",
        "status",
        "publication_date",
    )

