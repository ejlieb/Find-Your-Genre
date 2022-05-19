from tkinter import CASCADE
from django.db import models

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True)
    genre_name = models.CharField(max_length=20)

class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.TextField()
    original_title = models.CharField(max_length=100)
    original_language = models.CharField(max_length=100)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    genres_id = models.ManyToManyField(Genre, related_name='movies')
    imdb_id = models.CharField(max_length=10, null=True)

class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    gender = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True)
    imdb_id = models.CharField(max_length=100, null=True)
    profile_path = models.CharField(max_length=500, null=True)
    filmographies = models.ManyToManyField(Movie, related_name='actors')

class MovieImage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    image_URL = models.CharField(max_length=500)