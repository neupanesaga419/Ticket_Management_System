from django.db import models
from django.core.validators import MinValueValidator

from showtime.models import Shows
from django.contrib.auth.models import User


class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booked_user")
    shows = models.ForeignKey(Shows, on_delete=models.CASCADE, related_name="shows_booked")
    booked_date = models.DateField(auto_now_add=True)
    seats = models.IntegerField(validators=[MinValueValidator(0)])
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)+ ' - ' + str(self.shows)