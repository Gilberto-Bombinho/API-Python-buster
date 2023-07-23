from django.urls import path
from .views import MovieView, MovieViewId, MovieOrderView

urlpatterns = [path("movies/", MovieView.as_view()),
               path("movies/<int:movie_id>/", MovieViewId.as_view()),
               path("movies/<int:movie_id>/orders/", MovieOrderView.as_view())
               ]