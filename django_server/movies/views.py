from django.shortcuts import render
import requests
from pprint import pprint
from .models import Genre, Movie, Actor, MovieImage


URL = 'https://api.themoviedb.org/3'
API_KEY = 'ca33ee1ba3a143bb89f377cdff3e719c'

def genre_register(request):
    path = '/genre/movie/list'
    params = {
        'api_key' : API_KEY,
        'language' : 'ko-KR' 
    }

    genres = requests.get(URL+path, params=params).json().get('genres')
    results = []
    # all_genres_id = list(Genre.objects.values_list('genre_id', flat = True))
    all_genres = list(Genre.objects.all())
    for genre in genres:
        instance = Genre()
        instance.genre_id = genre['id']
        instance.genre_name = genre['name']
        if instance not in all_genres:
            instance.save()
        else:
            results.append('중복입니다')
    context = {
        'results' : results,
    }
    
    return render(request, 'movies/register.html', context)
        

def movie_register(request):
    path = '/discover/movie'
    params = {
        'api_key' : API_KEY,
        'language' : 'ko-KR',
        'sort_by' : 'vote_average.desc',
        'include_adult': True,
        'include_video': True,
        'vote_count.gte': 1000,
        'vote_average.gte': 7.0,
        'with_genres': 18,
        'with_watch_monetization_types': 'flatrate',
        'page': 1,
    }
    results = []
    all_genres_id = list(Genre.objects.values_list('genre_id', flat = True))

    for genre in all_genres_id:
        temp = 0
        all_movies = list(Movie.objects.all())
        params['with_genres'] = genre
        for i in range(1, 20):
            params['page'] = i
            movies = requests.get(URL+path, params=params).json().get('results')
            
            for movie in movies:
                instance = Movie(
                    movie_id=movie['id'],
                    title=movie['title'],
                    overview=movie['overview'],
                    release_date=movie['release_date'],
                    poster_path=movie['poster_path'],
                    original_title=movie['original_title'],
                    original_language=movie['original_language'],
                    vote_count=movie['vote_count'],
                    vote_average=movie['vote_average'],
                )
                if instance not in all_movies:
                    instance.save()

                    for genre_id in movie['genre_ids']:
                        genre_instance = Genre.objects.get(genre_id=genre_id)
                        instance.genres_id.add(genre_instance)
                    instance.save()
                    temp += 1

            genre_name = list(Genre.objects.filter(genre_id=genre).values_list('genre_name', flat = True))[0]
            results.append(f'{genre_name} : {temp}')                 

    context = {
        'results' : results,
    }
    
    return render(request, 'movies/register.html', context)


def movie_imdb_register(request):
    all_movie_ids = list(Movie.objects.all().values_list('movie_id', flat=True))
    results = 0
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR'
    }

    for movie_id in all_movie_ids:
        path = f'/movie/{movie_id}'
        imdb_id = requests.get(URL+path, params=params).json().get('imdb_id')
        movie = Movie.objects.get(movie_id=movie_id)
        movie.imdb_id = imdb_id
        movie.save()
        results += 1
    
    context = {
        'results' : results,
    }

    return render(request, 'movies/register.html', context)


def movie_images_register(request):
    all_movie_ids = list(Movie.objects.all().values_list('movie_id', flat=True))
    temp = 0
    params = {
    'api_key': API_KEY,
    }
    
    for movie_id in all_movie_ids:
        path = f'/movie/{movie_id}/images'
        movie = Movie.objects.get(movie_id=movie_id)
        images = requests.get(URL+path, params=params).json()['backdrops'][:3]
        for image in images:
            image_instance = MovieImage()
            image_instance.movie = movie
            image_instance.image_URL = 'https://www.themoviedb.org/t/p/original' + image['file_path']
            image_instance.save()
            temp += 1

    context = {
        'results': temp
    }

    return render(request, 'movies/register.html', context)




def actor_register(request):
   
    results = []
    temp = 0

    all_movie_ids = list(Movie.objects.all().values_list('movie_id', flat=True))
    params = {
        'api_key': API_KEY,
        'language': 'ko-KR'
    }
    
    for movie_id in all_movie_ids:
        movie = Movie.objects.get(movie_id=movie_id)
        path = f'/movie/{movie_id}/credits'
        movie_casts = requests.get(URL+path, params=params).json().get('cast')
        movie_casts.sort(key=lambda x: x['popularity'], reverse=True)
        movie_casts = movie_casts[:5]  # 영화당 5명만 저장할 것

        this_movie_cast = []
        for cast in movie_casts:
            results.append(cast['id'])  # 전체 목록과 비교
            this_movie_cast.append(cast['id'])  # 해당 영화의 캐스트 목록 
                
        for actor_id in this_movie_cast:
            path = f'/person/{actor_id}'
            actor = requests.get(URL+path, params=params).json()
            actor_instance = Actor(
                actor_id=actor['id'],
                gender=actor['gender'],
                name=actor['name'],
                biography=actor['biography'],
                imdb_id=actor['imdb_id'],
                profile_path=actor['profile_path'],     
            )
            if not Actor.objects.filter(actor_id=actor_id).exists():
                actor_instance.save()
                temp += 1
            else:
                actor_instance = Actor.objects.get(actor_id=actor_id) 
            actor_instance.filmographies.add(movie)
            actor_instance.save()
    
    context = {
        'results' : results,
        'temp' : temp,
    }
    
    return render(request, 'movies/register.html', context)





