from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from .models import GenreCounts
from movies.models import Movie, Genre



User = get_user_model()

@api_view(['POST',])
def likes_movie(request):
    # 좋아요 누른 영화 목록과 username을 받아온다
    movie_ids = request.data.get('likeMovieIds')
    username = request.data.get('username')
    
    # username으로 해당 유저를 조회함 
    user = User.objects.get(username=username)
    

    # 받은 영화 목록을 유저의 좋아요 영화 목록에 추가함 
    for movie_id in movie_ids:
        movie = Movie.objects.get(movie_id=movie_id)
        user.movie_likes.add(movie)
        genres = list(movie.genres_id.all())  # 장르 객체들의 리스트
        
        # results = GenreCounts.objects.filter(genre=genre, user=user)
        for genre in genres:
            genre_cnt = list(GenreCounts.objects.filter(genre=genre, user=user))
            if genre_cnt:
                genre_cnt[0].genre_cnt += 1
                genre_cnt[0].save()
            else:
                genre_cnt = GenreCounts(genre=genre, user=user)
                genre_cnt.genre_cnt = 1
                genre_cnt.save()
    
    beloved_genre = GenreCounts.objects.filter(user=user).order_by('-genre_cnt')[:1][0].genre
    
    # 받은 영화의 장르를 장르 카운트에 반영해줌 
    results = {
        'beloved_genre_id': beloved_genre.genre_id,
        'beloved_genre_name': beloved_genre.genre_name
    }
    
    return Response(results)  


@api_view(['POST',])
def dislikes_movie(reuqest):
    pass
    

'''
이후 가장 좋아하는 장르를 추출해서 API로 정보를 쏴주어야 함.
어떻게 좋아하는 장르를 빠른 시간 내에 추출할 수 있을까?
1) 해당 User가 좋아하는 영화들 목록을 추출 (-> 이건 빠름)
2) 추출된 영화 목록을 순회 (-> 이건 n배 늘어남)
3) 해당 영화가 속한 장르들 누적해서 세어 줌  (-> 이걸 따로 칼럼에 적어주는 게 나을까?)
   어차피 영화를 좋아할 때만 좋아하는 장르가 달라지니 기록해주는 게 나을 듯.  
'''


# User 데이터를 보내면서 좋아하는 영화의 모든 정보까지 다 보낸다 
@api_view(['GET'])
def profile(request, username):  # 해당 request에 username이 함께 옴
    profile_user = get_object_or_404(User, username=username)
    
    serializer = UserProfileSerializer(profile_user)

    return Response(serializer.data)

    



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
        