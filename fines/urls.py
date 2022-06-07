from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FineViewset


router = DefaultRouter()
router.register("", FineViewset, basename="fines")

urlpatterns = [
    path("", include(router.urls)),
]
