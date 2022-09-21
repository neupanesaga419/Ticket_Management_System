from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('showtime.urls')),
    path('movies/', include('movie.urls')),
    path('studios/', include('Studio.urls')),
    path('accounts/', include('accounts.urls')),
    path('tickets/', include('tickets.urls')),
    path('bookings/', include('bookings.urls')),
    path('userprofiles/', include('userprofiles.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()