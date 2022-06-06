from rest_framework import serializers

from library.models import BookItem
from .models import BorrowedBook


class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ("id", "book", "barcode", "status", "publication_date")


class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ("id", "book_item", "borrower", "borrowed_date", "due_date")

    book_item = BookItemSerializer()


class BorrowedBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ("book_item", "borrower", "borrowed_date", "due_date")
