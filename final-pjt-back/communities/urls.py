from django.urls import path
from . import views


app_name = 'communities'

urlpatterns = [
    path('<int:movie_id>/review_create/', views.review_create),
    
]