from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('showtime.urls')),
    path('movie/', include('movie.urls')),
    path('studio/', include('Studio.urls'))
]
