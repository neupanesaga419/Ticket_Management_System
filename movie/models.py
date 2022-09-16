from operator import mod
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=255)
    movie_details = models.TextField()
    released_data = models.DateField()
    date_created = models.DateField(auto_now_add=True)
    is_availiable = models.BooleanField(default=True)

    def __str__(self):
        return self.name
