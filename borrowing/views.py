from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from accounts.permissions import IsAdminOrLibrarian
from library.models import BookItem
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
    permission_classes = [IsAdminOrLibrarian]

    def get_serializer_class(self):
        if self.action in ("create"):
            return BorrowedBookCreateSerializer
        return BorrowedBookSerializer
