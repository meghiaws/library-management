from django.contrib import admin

from .models import BorrowedBook


@admin.register(BorrowedBook)
class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book_item_id",
        "borrower_id",
        "borrowed_date",
        "due_date",
    )