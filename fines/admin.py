from django.contrib import admin

from .models import Fine


@admin.register(Fine)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "borrowed_book",
        "member_id",
        "amount",
    )
