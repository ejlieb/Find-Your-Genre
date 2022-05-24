from django.urls import path
from . import views


app_name = 'communities'

urlpatterns = [

    # 리뷰 작성, 조회 및 좋아요/싫어요
    path('<int:movie_id>/review_create/', views.review_create),
    path('<int:movie_id>/<int:review_pk>/', views.review_detail),
    path('<int:movie_id>/<int:review_pk>/good/', views.review_good),
    path('<int:movie_id>/<int:review_pk>/bad/', views.review_bad),
  
    # 장르별 리뷰 모음 신청
    path('genre-reviews/<int:genre_sort_id>/', views.genre_review_list),

]