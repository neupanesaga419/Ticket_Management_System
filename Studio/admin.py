from django.contrib import admin
from Studio.models import Studio


@admin.register(Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display  = ['id','name','studio_details','studio_type','still_playing','capacity']

