from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api.views import MemberViewset, LibrarianViewset


router = DefaultRouter()
router.register("members", MemberViewset, basename="members")
router.register("librarians", LibrarianViewset, basename="librarians")

urlpatterns = [
    path("", include(router.urls)),
]