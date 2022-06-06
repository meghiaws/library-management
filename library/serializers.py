from rest_framework import serializers

from .models import Book, BookItem, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", "description")


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name", "description", "books")


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
        fields = ("id", "book", "barcode", "status", "publication_date")
