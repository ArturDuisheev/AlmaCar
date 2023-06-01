from rest_framework import routers

from .views import DetailCarViewSet, AwardViewSet, AboutCompanyViewSet

router = routers.DefaultRouter()
router.register(r'detailcar', DetailCarViewSet)
router.register(r'award', AwardViewSet)
router.register(r'AboutUs', AboutCompanyViewSet)

urlpatterns = router.urls
