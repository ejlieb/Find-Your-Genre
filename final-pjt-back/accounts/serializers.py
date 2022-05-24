from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import GenreCounts
from movies.models import Movie, Actor


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', )



class UserProfileSerializer(serializers.ModelSerializer):
    class UserProfileActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('actor_id', 'name', 'profile_path', )

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    class GenreCountSerializer(serializers.ModelSerializer):

        class Meta:
            model = GenreCounts
            fields = '__all__'


    movie_likes = MovieSerializer(many=True, read_only=True)
    genre_counts = GenreCountSerializer(read_only=True, many=True)
    
    class Meta:
        model = get_user_model()
        fields = '__all__'
        