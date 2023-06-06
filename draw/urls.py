from django.urls import path, include
from rest_framework import routers
from .views import GameViewSet, OpenBoxAPIView
router = routers.DefaultRouter()
router.register(r'game', GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('open-box/', OpenBoxAPIView.as_view())
]