from django.contrib.auth import get_user_model

from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import mixins

from .models import Librarian, Member
from .permissions import IsAdminOrLibrarian
from .serializers import (
    MemberSerializer,
    CreateMemberSerializer,
)


User = get_user_model()


class MemberViewset(ModelViewSet):
    queryset = Member.objects.select_related("user").all()
    permission_classes = [IsAdminOrLibrarian]


    def get_serializer_class(self):
        if self.action == "create":
            return CreateMemberSerializer
        return MemberSerializer

    def perform_destroy(self, instance):
        instance.user.delete()
        return super().perform_destroy(instance)
