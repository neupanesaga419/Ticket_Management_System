from rest_framework.routers import DefaultRouter
from Studio.views import StudioAPIView

router = DefaultRouter()
router.register(r'studio', StudioAPIView, basename="studio")

urlpatterns  = router.urls