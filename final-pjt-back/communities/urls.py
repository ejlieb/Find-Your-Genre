from django.urls import path
from . import views


app_name = 'communities'

urlpatterns = [
    path('<int:movie_id>/review_create/', views.review_create),
    path('<int:movie_id>/<int:review_pk>/', views.review_detail),
    path('<int:movie_id>/<int:review_pk>/good/', views.review_good),
    
]