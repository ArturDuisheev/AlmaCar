from rest_framework import routers

from .views import OurCarViewSet, DetailCarViewSet, AwardViewSet

router = routers.DefaultRouter()
router.register(r'ourcar', OurCarViewSet)
router.register(r'detailcar', DetailCarViewSet)
router.register(r'award', AwardViewSet)

urlpatterns = router.urls
