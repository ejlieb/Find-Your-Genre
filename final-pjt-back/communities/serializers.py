from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review, Comment



class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fiels = ('content',)




