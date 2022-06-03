from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.generics import CreateAPIView

from .models import Member
from .serializers import MemberSerializer


class MemberViewset(ModelViewSet):
    queryset = Member.objects.select_related("user").all()
    serializer_class = MemberSerializer

