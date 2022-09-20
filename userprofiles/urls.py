from rest_framework.routers import DefaultRouter

from userprofiles.views import UserProfileViewSet

router = DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename="profile")

urlpatterns = router.urls