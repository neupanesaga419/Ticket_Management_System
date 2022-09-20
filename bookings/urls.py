from django.urls import path

from bookings.views import BookingsDetails, ViewBookings

urlpatterns = [
    path("booking/", ViewBookings.as_view(), name="list-create-tickets"),
    path("<int:pk>", BookingsDetails.as_view(), name="ticket-details"),
]