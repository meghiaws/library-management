from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api.views import BorrowedBookViewset


router = DefaultRouter()
router.register("books", BorrowedBookViewset, basename="borrowed-books")


urlpatterns = [
    path("", include(router.urls)),
]
