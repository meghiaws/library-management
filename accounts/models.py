from django.db import models
from django.conf import settings

from .managers import MemberManager, LibrarianManager


class Librarian(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    staff_code = models.CharField(max_length=8)

    objects = LibrarianManager()

    def __str__(self):
        return f"Librarian: {self.user.username}"


class Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership_code = models.CharField(max_length=8)

    objects = MemberManager()

    def __str__(self):
        return f"Member: {self.user.username}"
