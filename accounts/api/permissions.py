from rest_framework.permissions import BasePermission
from accounts.models import Librarian


class IsAdminOrLibrarian(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if Librarian.objects.filter(user=request.user).exists():
            return True
        return False
