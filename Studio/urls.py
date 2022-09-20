from rest_framework.routers import DefaultRouter
from Studio.views import StudioAPIView

router = DefaultRouter()
router.register(r'', StudioAPIView, basename="studio")

urlpatterns  = router.urls