from django.contrib import admin

from .models import ReservedBook


@admin.register(ReservedBook)
class ReservedBookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "book_item_id",
        "reserver_id",
        "reserved_at",
        "due_time",
    )