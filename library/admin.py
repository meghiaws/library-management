from django.contrib import admin
from .models import Author, Book, BookItem, BorrowedBook


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(BorrowedBook)
