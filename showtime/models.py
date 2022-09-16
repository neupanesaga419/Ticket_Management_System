from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from dateutil import tz

from movie.models import Movie
from Studio.models import Studio


SHOW_TYPES = (
        ("MORNING SHOW","MORNING SHOW"),
        ("AFTERNOON SHOW","AFTERNOON SHOW"),
        ("EVENING SHOW","EVENING SHOW"),
        ("NIGHT SHOW","NIGHT SHOW")
        )

to_local = tz.gettz('Asia/Kathmandu')

def validate_time(data):
    date_today = datetime.now()
    if date_today.astimezone(to_local) > data:
        raise ValidationError("show start time must be greater than today's time.")


class ShowTime(models.Model):

    show_start_time = models.DateTimeField(validators=[validate_time])
    show_end_time = models.DateTimeField(validators=[validate_time])
    date_created = models.DateField(auto_now_add=True)
    show_type = models.CharField(choices=SHOW_TYPES, max_length=150)

    def __str__(self):
        show_start_time = self.show_start_time.astimezone(to_local)
        msg = f"{self.show_type} - {show_start_time.strftime('%I:%M %p')}"
        return msg



class Shows(models.Model):
    show_time = models.ForeignKey(ShowTime, on_delete=models.DO_NOTHING, related_name="show_time")
    studio = models.ForeignKey(Studio, on_delete=models.DO_NOTHING, related_name="studio")
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING, related_name="movie")
    date_created = models.DateField(auto_now_add=True)
    still_playing = models.BooleanField(default=True)

    def __str__(self):
        msg = f"{self.show_time.show_type} - {self.studio.name} - {self.movie.name}"
        return msg