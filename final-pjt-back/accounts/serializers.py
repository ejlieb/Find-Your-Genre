from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', )



class UserProfileSerializer(serializers.ModelSerializer):
    

    class MovieSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = '__all__'

    movie_likes = MovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = '__all__'