from rest_framework import serializers
from .models import Genre, Movie, MovieImage


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fiels = '__all__'


class SignupMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'poster_path', 'genres',)


class MovieSerializerWithImages(serializers.ModelSerializer):
    
    class GenreNestedSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('genre_id', 'genre_name',)
    

    class MovieImageSerializer(serializers.ModelSerializer):
        class Meta:
            model = MovieImage
            fields = ('image_URL',)

    genres = GenreNestedSerializer(many=True, read_only=True)
    movieimage_set = MovieImageSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
