from django.contrib import admin

from userprofiles.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = ["id", "user", "full_name", "address", "age", "gender", "profile_image"]