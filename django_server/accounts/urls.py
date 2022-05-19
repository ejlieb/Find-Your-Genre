from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    # 회원가입 페이지
    path('signup/', views.signup)

]