from django.urls import path

from userprofiles.views import ViewProfile, UserProfileDetails

urlpatterns = [
    path("prof", ViewProfile.as_view(), name="userprofile"),
    path("<int:pk>/", UserProfileDetails.as_view(), name="userprofile-details"),
]
