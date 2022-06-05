from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from .models import Member


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "password", "email", "first_name", "last_name")


class CreateMemberSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = ("user",)

    def save(self, **kwargs):
        user = self.validated_data["user"]
        self.instance = Member.objects.create_member(
            username=user["username"],
            password=user["password"],
            email=user["email"],
            first_name=user["first_name"],
            last_name=user["last_name"],
        )
        return self.instance


class MemberSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Member
        fields = ("id", "membership_code", "user")
