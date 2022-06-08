from django_filters import rest_framework as filters

from ..models import Book, Author, BookItem


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Author
        fields = ["name"]


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    author__name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ["title", "isbn", "author", "author__name"]


class BookItemFilter(filters.FilterSet):
    from_date = filters.DateFilter(field_name="publication_date", lookup_expr="gte")
    to_date = filters.DateFilter(field_name="publication_date", lookup_expr="lte")

    class Meta:
        model = BookItem
        fields = ["barcode", "status", "from_date", "to_date"]
