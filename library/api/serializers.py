from rest_framework import serializers

from ..models import Book, BookItem, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name", "description")


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name", "description", "books")


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ("id", "title", "isbn", "author", "subject", "page_counts")


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "isbn", "author", "subject", "page_counts")


class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ("id", "book", "barcode", "status", "publication_date")

    book = BookSerializer()


class BookItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ("id", "barcode", "status", "publication_date")

    def create(self, validated_data):
        book_id = self.context["book_id"]
        return BookItem.objects.create(book_id=book_id, **validated_data)
