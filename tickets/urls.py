from django.urls import path

from tickets.views import TicketDetails, ViewTickets


urlpatterns = [
    path("", ViewTickets.as_view(), name="list-create-tickets"),
    path("<int:pk>", TicketDetails.as_view(), name="ticket-details"),
]