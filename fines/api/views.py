from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from accounts.api.permissions import IsAdminOrLibrarian
from ..models import Fine
from .serializers import FineSerializer


class FineViewset(
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Fine.objects.select_related(
        "member", 
        "member__user", 
        "borrowed_book", 
        "borrowed_book__book_item"
    ).all()    
    serializer_class = FineSerializer
    permission_classes = [IsAdminOrLibrarian]
