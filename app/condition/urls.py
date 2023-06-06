from rest_framework import routers

from .views import CardInConditionViewSet

router = routers.DefaultRouter()
router.register(r'ConditionCard', CardInConditionViewSet)

urlpatterns = router.urls