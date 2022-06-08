from rest_framework.viewsets import ModelViewSet

from ..models import Book, BookItem, Author
from .filters import AuthorFilter, BookFilter, BookItemFilter
from .serializers import (
    BookSerializer,
    BookCreateUpdateSerializer,
    AuthorSerializer,
    AuthorListSerializer,
    BookItemSerializer,
    BookItemCreateUpdateSerializer,
)


class BookViewset(ModelViewSet):
    queryset = Book.objects.prefetch_related("author").all()
    filterset_class = BookFilter

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return BookCreateUpdateSerializer
        return BookSerializer


class AuthorViewset(ModelViewSet):
    filterset_class = AuthorFilter

    def get_queryset(self):
        if self.action == "list":
            Author.objects.prefetch_related("books").all()
        return Author.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return AuthorListSerializer
        return AuthorSerializer


class BookItemViewSet(ModelViewSet):
    filterset_class = BookItemFilter

    def get_queryset(self):
        return (
            BookItem.objects
                .select_related("book")
                .prefetch_related("book__author")
                .filter(book=self.kwargs["book_pk"])
        )

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return BookItemCreateUpdateSerializer
        return BookItemSerializer

    def get_serializer_context(self):
        return {"book_id": self.kwargs["book_pk"]}