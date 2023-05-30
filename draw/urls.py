from django.urls import path, include
from rest_framework import routers
from .views import BoxViewSet, PrizeViewSet, MoreInfoViewSet

router = routers.DefaultRouter()
router.register(r'boxes', BoxViewSet)
router.register(r'prizes', PrizeViewSet)
router.register(r'moreinfo', MoreInfoViewSet)
# router.register(r'rental', RentalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]