from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    # 좋아요한 영화 등록하기
    path('likes_movie/', views.likes_movie),

    # 프로필 페이지
    path('profile/<str:username>/', views.profile),

    # 회원가입 페이지
    # path('signup/', views.signup)
]