from django.db import models
from showtime.models import Shows
from django.contrib.auth.models import User


class Tickets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ticket_related")
    shows = models.ForeignKey(Shows, on_delete=models.CASCADE, related_name="shows_purchased")
    purchased_date = models.DateField(auto_now_add=True)
    seats = models.IntegerField()
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user.username)+ ' - ' + str(self.shows)