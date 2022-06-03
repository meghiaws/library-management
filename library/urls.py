from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MemberViewset


router = DefaultRouter()
router.register("members", MemberViewset, basename="members")

urlpatterns = [
    path("", include(router.urls)),
]