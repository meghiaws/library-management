from rest_framework.serializers import ModelSerializer

from library.models import Member
from core.serializers import UserSerializer


class MemberSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ("membership_code", "user")

    user = UserSerializer()