from django.urls import path
import showtime.views as svi

urlpatterns = [
    path('showtime/', svi.ShowTimeListAV.as_view(), name="showtime-list"),
    path('showtime/<pk>/', svi.ShowTimeDetailAV.as_view(), name="showtime-detail"),
    path('shows/', svi.ShowsListAV.as_view(), name="shows-list"),
    path('shows/create/', svi.ShowsCreateAV.as_view(), name='show-create'),
    path('shows_detail/<pk>/', svi.ShowsDetailsAV.as_view(), name='shows-detail'),
]