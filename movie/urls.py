from django.urls import path
import movie.views as mvi


urlpatterns = [
    path('', mvi.GetMovieAV.as_view(), name="movie-list"),
    path('<pk>', mvi.MovieDetailAV.as_view(), name="movie-detail"),
    path('create', mvi.CreateMovieAV.as_view(), name="movie-create"),
    path('update_delete/<pk>', mvi.UpdateAV.as_view(), name="movie-update-delete"),
]

