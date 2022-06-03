from django.contrib import admin
from .models import Member, Librarian, Author, Book, BookItem, BorrowedBook


admin.site.register(Member)
admin.site.register(Librarian)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookItem)
admin.site.register(BorrowedBook)
