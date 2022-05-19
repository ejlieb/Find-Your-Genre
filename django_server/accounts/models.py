from django.contrib.auth.models import AbstractUser
from django.db import models
from movies.models import Movie

class User(AbstractUser):
    followings = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followers')
    movie_list = models.ManyToManyField(Movie, related_name = 'listing_users')
    movie_likes = models.ManyToManyField(Movie, related_name = 'liking_users')
    # article_likes = models.ManyToManyField
    # comment_likes
    # 

    pass
