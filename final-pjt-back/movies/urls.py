from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('signup_movies/', views.signup_movies),
    path('main_page_recommend/', views.main_page_recommend),
    path('search/', views.search),
    path('detail/<int:movie_id>/', views.movie_detail),



    # 영화 추천하는 url 모음
    # path('genre_recommend/<int:genre_sort>', views.genre_recommend),
    path('genre_top_ten/<int:genre_sort>', views.genre_top_ten),

    
    



    # 이하는 TMDB서버에서 장고 서버로 데이터 받아오는 URL
    # path('genre/', views.genre_register),
    # path('movie/', views.movie_register),
    # path('actor/', views.actor_register),
    # path('movie_imdb_register/', views.movie_imdb_register),
    # path('movie_images_register/', views.movie_images_register),
]