from rest_framework import serializers

from accounts.api.serializers import MemberSerializer
from borrowing.api.serializers import BorrowedBookSerializer

from library.models import BookItem
from ..models import Fine


class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ("id", "book", "barcode", "status", "publication_date")


class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = ("id", "member", "borrowed_book", "amount")

    member = MemberSerializer()
    borrowed_book = BorrowedBookSerializer()
