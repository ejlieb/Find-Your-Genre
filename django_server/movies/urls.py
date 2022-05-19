from django.urls import path
from . import views


urlpatterns = [
    path('genre/', views.genre_register),
    path('movie/', views.movie_register),
    path('actor/', views.actor_register),
    path('movie_imdb_register/', views.movie_imdb_register),
    path('movie_images_register/', views.movie_images_register),
]