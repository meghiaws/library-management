from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from .models import BorrowedBook
from .serializers import BorrowedBookSerializer, BorrowedBookCreateSerializer


class BorrowedBookViewset(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = BorrowedBook.objects.select_related("book_item").all()

    def get_serializer_class(self):
        if self.action in ("create"):
            return BorrowedBookCreateSerializer
        return BorrowedBookSerializer
