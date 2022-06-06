from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ReservedBookViewset


router = DefaultRouter()
router.register("books", ReservedBookViewset, basename="reserved-books")


urlpatterns = [
    path("", include(router.urls)),
]
