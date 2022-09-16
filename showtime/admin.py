from django.contrib import admin
from showtime.models import ShowTime, Shows

@admin.register(ShowTime)
class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'show_start_time', 'show_end_time', 'date_created', 'show_type']


@admin.register(Shows)
class ShowsAdmin(admin.ModelAdmin):
    list_display = ['id', 'show_time', 'studio', 'movie', 'date_created', 'still_playing']