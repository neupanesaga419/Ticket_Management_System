from django.contrib import admin
from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'movie_details', 'released_data', 'date_created','is_availiable']

