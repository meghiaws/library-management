from django.db.models.manager import Manager
from django.contrib.auth import get_user_model

from .utils import create_random_8_digits_code


class MemberManager(Manager):
    def create_member(self, username, password, email, first_name, last_name):
        User = get_user_model()
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        membership_code = create_random_8_digits_code()
        return self.create(membership_code=membership_code, user=user)


class LibrarianManager(Manager):
    def create_librarian(self, username, password, email, first_name, last_name):
        User = get_user_model()
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        staff_code = create_random_8_digits_code()
        return self.create(staff_code=staff_code, user=user)
