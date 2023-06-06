from rest_framework import routers

from .views import ItemAdditionViewSet

router = routers.DefaultRouter()
router.register(r'Item', ItemAdditionViewSet)

urlpatterns = router.urls
