from django.contrib import admin
from .models import Member, Librarian


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "membership_code",
        "user",
    )

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "staff_code",
        "user",
    )
