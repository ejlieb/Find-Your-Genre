from rest_framework import serializers
from django.contrib.auth import get_user_model

from communities.models import Review
from .models import GenreCounts, ActorCounts
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
        genre_name = serializers.ReadOnlyField(source='counted_genre.genre_name')
        class Meta:
            model = GenreCounts
            fields = ('genre_name', 'genre_cnt',)

    class ActorCountSerializer(serializers.ModelSerializer):
        actor_id = serializers.ReadOnlyField(source='counted_actor.actor_id')
        actor_name = serializers.ReadOnlyField(source='counted_actor.name')

        class Meta:
            model = ActorCounts
            fields = ('actor_id', 'actor_name', 'actor_cnt',)

    class UserReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'
    

    movie_likes = MovieSerializer(many=True, read_only=True)
    genre_counts = GenreCountSerializer(source='genrecounts_set', read_only=True, many=True)
    actor_counts = ActorCountSerializer(source='actorcounts_set', read_only=True, many=True)
    review_set = UserReviewSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = get_user_model()
        exclude = ('counted_genres', )
        