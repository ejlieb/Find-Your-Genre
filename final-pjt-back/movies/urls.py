from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('test/', views.signup_movie_serializer)


    # 이하는 TMDB서버에서 장고 서버로 데이터 받아오는 URL
    # path('genre/', views.genre_register),
    # path('movie/', views.movie_register),
    # path('actor/', views.actor_register),
    # path('movie_imdb_register/', views.movie_imdb_register),
    # path('movie_images_register/', views.movie_images_register),
]