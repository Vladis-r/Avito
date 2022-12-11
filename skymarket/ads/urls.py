from django.urls import path, include
from rest_framework import routers

from ads.views import AdViewSet, CommentViewSet

# TODO настройка роутов для модели
router = routers.SimpleRouter()
router.register('ads', AdViewSet)
router.register('ad/<int:ad_id>/comment', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
