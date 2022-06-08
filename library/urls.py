from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter

from .api.views import BookViewset, AuthorViewset, BookItemViewSet


router = DefaultRouter()
router.register("books", BookViewset, basename="books")
router.register("authors", AuthorViewset, basename="authors")

books_router = NestedDefaultRouter(router, "books", lookup="book")
books_router.register("items", BookItemViewSet, basename="book-items")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(books_router.urls)),
]
