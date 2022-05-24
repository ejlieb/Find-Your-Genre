from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review, Comment
from movies.models import Movie



class ReviewSerializer(serializers.ModelSerializer):
    class ReviewUserSerializer(serializers.ModelSerializer):
            class Meta:
                model = get_user_model()
                fields = ('pk', 'username', )

    class MovieinReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('movie_id', 'title', 'poster_path')

    user = ReviewUserSerializer(read_only=True)
    user_good_eval = ReviewUserSerializer(many=True, read_only=True)
    good_eval_count = serializers.IntegerField(source='user_good_eval.count', read_only=True)
    user_bad_eval = ReviewUserSerializer(many=True, read_only=True)
    bad_eval_count = serializers.IntegerField(source='user_bad_eval.count', read_only=True)
    movie = MovieinReviewSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content', 'rating', )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fiels = ('content',)




