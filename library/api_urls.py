from django.urls import include, path

from rest_framework.routers import DefaultRouter

from book.api_views import BookViewSet
from order.api_views import OrderViewSet


router = DefaultRouter()

router.register(
    r'book',
    BookViewSet,
    basename='book'
)

router.register(
    r'order',
    OrderViewSet,
    basename='order'
)

urlpatterns = [
    path(
        '',
        include(router.urls)
    ),
]
