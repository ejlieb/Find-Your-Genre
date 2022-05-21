from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests, random
from pprint import pprint
from .models import Genre, Movie, Actor, MovieImage
from accounts.models import User, GenreCounts
from .serializers import SignupMovieSerializer, MovieSerializerWithImages

# 로그인을 하면서 동시에 좋아하는 영활를 고를 수 있도록 영화 360개를 송출합니다.
@api_view(['GET',])
def signup_movies(request):
    movies = get_list_or_404(Movie)
    # 평점이 매겨진 개수가 많은 순서대로 정렬을 하고 상위 360개만을 남깁니다.
    movies.sort(key=lambda x: x.vote_count, reverse=True)
    movies = movies[:360]
    random.shuffle(movies)  # 영화를 섞어줌 
    
    serializer = SignupMovieSerializer(movies, many=True)
    
    return Response(serializer.data)


# 장르페이지 이전 메인 화면에 최애 장르의 랜덤 영화 추천
# 로그인한 사용자라면 가장 좋아하는 장르의 id, 이름과 해당 장르 영화 3개 랜덤으로 추천받음
# 만일 로그인하지 않았다면, 적당히 유명하고 평점이 괜찮은 영화 하나를 랜덤으로 추천받음
@api_view(['GET',])  
def main_page_recommend(request):
    if request.user.is_authenticated:  
        now_user = User.objects.get(username=request.user)
        genre_set = list(GenreCounts.objects.filter(user=now_user))
        favorite_genre = genre_set[0]
        max_likes = 0
        for genre in genre_set:
            if genre.genre_cnt > max_likes:
                max_likes = genre.genre_cnt
                favorite_genre = genre.genre
        
        # 최애 장르의 영화들 추출
        favor_movies = list(favorite_genre.movies.all())
        favor_movies.sort(key=lambda x: (x.vote_count, x.vote_average), reverse=True)
        random.shuffle(favor_movies)
        favor_movies = favor_movies[:3]
        serializer = MovieSerializerWithImages(favor_movies, many=True)
            
    
        results = {
        'favorite_genre_id': favorite_genre.pk,
        'favorite_genre_name' : favorite_genre.genre_name,
        'favorite_genre_movies' : serializer.data,
        }
    
    else:
        movies = list(Movie.objects.filter(vote_count__gte=3000, vote_average__gte=8.0))
        random_movie = MovieSerializerWithImages(random.sample(movies, 1)[0])
    

    
        results = {
            'random_movie': random_movie.data,
        }
    return Response(results)


# 장르페이지 메인 화면에 트렌디한 영화를 장르를 섞어서 추천해줌
@api_view(['GET', 'POST',])  # api_view 무엇무엇을 허용?
def genre_page_recommend(request):
    pass


# 장르별 평점 순위 10 영화 추천 
@api_view(['GET', 'POST',])
def genre_top_ten(request):
    pass
'''
request로 해당 페이지의 장르 그룹을 받음. (1~7)
해당 장르 그룹에 포함된 장르의 영화들을 모두 조회함. (Genre.objects.filter)
각 그룹당 10개씩 뽑아서 넣고 random.shuffle로 섞어준 다음에 10개를 뽑아서 보내줌
'''



# 좋아하는 배우가 나오는 영화들 무작위 추천
@api_view(['GET', 'POST'])
def actor_top_ten(request):
    pass

'''
좋아하는 배우가 나오는 영화를 추천함
만일 좋아하는 배우가 3명 미만인 경우 ==> 자신이 좋아하는 영화 중 가장 많이 등장한 배우의 필모그래피들을 섞어줌
'''



# 각 세부 장르별 추천
@api_view(['GET', 'POST'])
def each_genre_recommend(request):
    '''
    각 세부 장르에서 추천되는 영화는 겹치면 안 됨

    '''
    pass

'''
요청이 온 장르 그룹에 속하는 영화들 중에서 평점 높은 순으로 50개를 뽑고 랜덤 10개씩 추출
'''


# 트렌딩 카루셀 따로 만들기


# #  이하는 Data 받아오는 함수
# URL = 'https://api.themoviedb.org/3'
# API_KEY = 'ca33ee1ba3a143bb89f377cdff3e719c'

# def genre_register(request):
#     path = '/genre/movie/list'
#     params = {
#         'api_key' : API_KEY,
#         'language' : 'ko-KR' 
#     }

#     genres = requests.get(URL+path, params=params).json().get('genres')
#     results = []
#     # all_genres_id = list(Genre.objects.values_list('genre_id', flat = True))
#     all_genres = list(Genre.objects.all())
#     for genre in genres:
#         instance = Genre()
#         instance.genre_id = genre['id']
#         instance.genre_name = genre['name']
#         if instance not in all_genres:
#             instance.save()
#         else:
#             results.append('중복입니다')
#     context = {
#         'results' : results,
#     }
    
#     return render(request, 'movies/register.html', context)
        

# def movie_register(request):
#     path = '/discover/movie'
#     params = {
#         'api_key' : API_KEY,
#         'language' : 'ko-KR',
#         'sort_by' : 'vote_average.desc',
#         'include_adult': True,
#         'include_video': True,
#         'vote_count.gte': 1000,
#         'vote_average.gte': 7.0,
#         'with_genres': 18,
#         'with_watch_monetization_types': 'flatrate',
#         'page': 1,
#     }
#     results = []
#     all_genres_id = list(Genre.objects.values_list('genre_id', flat = True))

#     for genre in all_genres_id:
#         temp = 0
#         all_movies = list(Movie.objects.all())
#         params['with_genres'] = genre
#         for i in range(1, 20):
#             params['page'] = i
#             movies = requests.get(URL+path, params=params).json().get('results')
            
#             for movie in movies:
#                 instance = Movie(
#                     movie_id=movie['id'],
#                     title=movie['title'],
#                     overview=movie['overview'],
#                     release_date=movie['release_date'],
#                     poster_path=movie['poster_path'],
#                     original_title=movie['original_title'],
#                     original_language=movie['original_language'],
#                     vote_count=movie['vote_count'],
#                     vote_average=movie['vote_average'],
#                 )
#                 if instance not in all_movies:
#                     instance.save()

#                     for genre_id in movie['genre_ids']:
#                         genre_instance = Genre.objects.get(genre_id=genre_id)
#                         instance.genres_id.add(genre_instance)
#                     instance.save()
#                     temp += 1

#             genre_name = list(Genre.objects.filter(genre_id=genre).values_list('genre_name', flat = True))[0]
#             results.append(f'{genre_name} : {temp}')                 

#     context = {
#         'results' : results,
#     }
    
#     return render(request, 'movies/register.html', context)


# def movie_imdb_register(request):
#     all_movie_ids = list(Movie.objects.all().values_list('movie_id', flat=True))
#     results = 0
#     params = {
#         'api_key': API_KEY,
#         'language': 'ko-KR'
#     }

#     for movie_id in all_movie_ids:
#         path = f'/movie/{movie_id}'
#         imdb_id = requests.get(URL+path, params=params).json().get('imdb_id')
#         movie = Movie.objects.get(movie_id=movie_id)
#         movie.imdb_id = imdb_id
#         movie.save()
#         results += 1
    
#     context = {
#         'results' : results,
#     }

#     return render(request, 'movies/register.html', context)


# def movie_images_register(request):
#     all_movie_ids = list(Movie.objects.all().values_list('movie_id', flat=True))
#     temp = 0
#     params = {
#     'api_key': API_KEY,
#     }
    
#     for movie_id in all_movie_ids:
#         path = f'/movie/{movie_id}/images'
#         movie = Movie.objects.get(movie_id=movie_id)
#         images = requests.get(URL+path, params=params).json()['backdrops'][:3]
#         for image in images:
#             image_instance = MovieImage()
#             image_instance.movie = movie
#             image_instance.image_URL = 'https://www.themoviedb.org/t/p/original' + image['file_path']
#             image_instance.save()
#             temp += 1

#     context = {
#         'results': temp
#     }

#     return render(request, 'movies/register.html', context)




# def actor_register(request):
   
#     results = []
#     temp = 0

#     all_movie_ids = list(Movie.objects.all().values_list('movie_id', flat=True))
#     params = {
#         'api_key': API_KEY,
#         'language': 'ko-KR'
#     }
    
#     for movie_id in all_movie_ids:
#         movie = Movie.objects.get(movie_id=movie_id)
#         path = f'/movie/{movie_id}/credits'
#         movie_casts = requests.get(URL+path, params=params).json().get('cast')
#         movie_casts.sort(key=lambda x: x['popularity'], reverse=True)
#         movie_casts = movie_casts[:5]  # 영화당 5명만 저장할 것

#         this_movie_cast = []
#         for cast in movie_casts:
#             results.append(cast['id'])  # 전체 목록과 비교
#             this_movie_cast.append(cast['id'])  # 해당 영화의 캐스트 목록 
                
#         for actor_id in this_movie_cast:
#             path = f'/person/{actor_id}'
#             actor = requests.get(URL+path, params=params).json()
#             actor_instance = Actor(
#                 actor_id=actor['id'],
#                 gender=actor['gender'],
#                 name=actor['name'],
#                 biography=actor['biography'],
#                 imdb_id=actor['imdb_id'],
#                 profile_path=actor['profile_path'],     
#             )
#             if not Actor.objects.filter(actor_id=actor_id).exists():
#                 actor_instance.save()
#                 temp += 1
#             else:
#                 actor_instance = Actor.objects.get(actor_id=actor_id) 
#             actor_instance.filmographies.add(movie)
#             actor_instance.save()
    
#     context = {
#         'results' : results,
#         'temp' : temp,
#     }
    
#     return render(request, 'movies/register.html', context)





