from django.db import models
from django.conf import settings
from movies.models import Movie


# class Review(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     title = models.CharField(max_length=30)
#     content = models.TextField()
#     user_good_eval = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, related_name='good_reviews')
#     user_bad_eval = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True, related_name='bad_reviews')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
    


# class Comment(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
#     content = models.CharField(max_length=150)
#     created_at = models.DateTimeField(auto_now_add=True)


