from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from movies.models import Movie



User = get_user_model()

@api_view(['GET', 'POST'])
def likes_movie(request):
    movie_ids = request.data.get('likedMovieIds')
    # username = request.data.get('username')
    # user = User.objects.get(username=username)
    
    # for movie_id in movie_ids:
    #     movie = Movie.objects.get(movie_id=movie_id)
    #     user.movie_likes.add(movie)

    return Response(request)
    


    




# @api_view(['POST'])
# def signup(request):
#     password = request.data.get('password')
#     password_confirm = request.data.get('password2')

#     # if password != password_confirm:
#     #     error_msg = {
#     #         'error' : '비밀번호 불일치',
#     #     }
#     #     return Response(error_msg, status=status.HTTP_400_BAD_REQUEST)
    
#     # serializer = UserSerializer(data=request.data)

#     # if serializer.is_valid(raise_exception=True):
#     #     user = serializer.save()
        