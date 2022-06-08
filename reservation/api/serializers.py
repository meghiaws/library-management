from rest_framework import serializers

from library.models import BookItem
from ..models import ReservedBook


class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ("id", "book", "barcode", "status", "publication_date")


class ReservedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservedBook
        fields = ("id", "book_item", "reserver", "reserved_at", "due_time")

    book_item = BookItemSerializer()


class ReservedBookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservedBook
        fields = ("book_item", "reserver", "reserved_at", "due_time")
