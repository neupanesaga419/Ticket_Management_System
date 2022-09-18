from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
import accounts.views as avi

urlpatterns = [
    path("register/", avi.register_user, name="register"),
    path("login/", avi.CustomTokenObtainPairView.as_view(), name="login"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]