from django.urls import path

from tickets.views import ViewTickets


urlpatterns = [
    path("", ViewTickets.as_view(), name="list-create-tickets"),
]