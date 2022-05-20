from django.contrib.auth.models import AbstractUser
from django.db import models
from movies.models import Movie, Genre

class User(AbstractUser):
    followings = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')
    movie_list = models.ManyToManyField(Movie, related_name = 'listing_users')  # 찜한 영화 등록
    movie_likes = models.ManyToManyField(Movie, related_name = 'liking_users')  # 좋아요한 영화 등록
    genre_counts = models.ManyToManyField(Genre, through='GenreCounts')
    # article_likes = models.ManyToManyField
    # comment_likes
    # 


class GenreCounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    genre_cnt = models.IntegerField(default=0)


# signin의 과정은 어떻게 진행될까?
# Vue Client에게 API 요청을 받아 user_serializer를 전송함
# user_serializer를 전송받은 Vue는 화면을 적절하게 렌더링하여 방문자에게 제공
# 방문자는 Vue가 렌더링해준 페이지를 채워서 전송해줌
# 