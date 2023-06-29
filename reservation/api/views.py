from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from accounts.api.permissions import IsAdminOrLibrarian

from ..models import ReservedBook
from .serializers import ReservedBookSerializer, ReservedBookCreateSerializer


class ReservedBookViewset(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = ReservedBook.objects.select_related("book_item").all()
    # permission_classes = [IsAdminOrLibrarian]

    def get_serializer_class(self):
        if self.action in ("create"):
            return ReservedBookCreateSerializer
        return ReservedBookSerializer
