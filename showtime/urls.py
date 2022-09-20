# from email.mime import base
# from django.urls import path
# import showtime.views as showtimeview

from showtime.views import ShowTimeAPIView, ShowsAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'showtime', ShowTimeAPIView, basename='showtime')
router.register(r'', ShowsAPIView, basename="shows")


urlpatterns = router.urls