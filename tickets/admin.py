from django.contrib import admin
from tickets.models import Tickets


@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):

    list_display = ["id","user",'shows','purchased_date','is_valid']