from rest_framework import routers

from .views import DetailCarViewSet, AwardViewSet, AboutCompanyViewSet, RentAutoView

router = routers.DefaultRouter()
router.register(r'detailcar', DetailCarViewSet)
router.register(r'award', AwardViewSet)
router.register(r'AboutUs', AboutCompanyViewSet)
router.register(r'rent_auto', RentAutoView)
urlpatterns = router.urls
