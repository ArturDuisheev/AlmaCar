from rest_framework import routers

from .views import ContactViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = router.urls
