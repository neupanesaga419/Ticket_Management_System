from movie.views import MovieAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movie', MovieAPIView, basename='movie')



urlpatterns = router.urls