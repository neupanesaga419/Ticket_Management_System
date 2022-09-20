from django.contrib import admin
from bookings.models import Bookings


@admin.register(Bookings)
class Booking(admin.ModelAdmin):

    list_display = ["id","user",'shows','seats','booked_date','is_paid']