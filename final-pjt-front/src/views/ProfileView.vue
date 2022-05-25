<template>
  <div class="container">
    <div class="for-nav"></div>
    <div class="profile-box">
      <p>{{profile}}</p>
      <div>
        <h1>{{ profile.username }}님의 프로필 페이지</h1>
        <div class="row">
          <div class="col-3">
            <h1>좋아하는 장르</h1>
          </div>
           <div class="liked-movie-box d-flex flex-column col-9">
              <div class="d-flex">
                <p class="liked-movie-p align-self-start mx-3">Favorite Actors</p>
              </div>
            
              <div class="liked-movie-img-box d-flex justify-content-center align-items-center">
                <div v-for=" (movie,index) in slicedMovieList" :key="index" class="liked-movie-img mx-3" :id="`movie-${index}`">
                  <!-- 클릭하면 영화 상세페이지로 가게 하기 -->
                  <img :src="poster_path + movie.poster_path" alt="" class="movie-img" @click="goToDetail(movie)">
                </div>
              </div>
            </div>
        </div>
      </div>
      
    <!-- <h1>{{ profile}}</h1> -->
    </div>
    
    <!-- 좋아요 누른 영화 -->
    <div class="row">
      <div class="liked-movie-box d-flex flex-column col-12">
        <div class="d-flex">
          <p class="liked-movie-p align-self-start mx-3">Liked Movies</p>
          <button type="button" class="btn btn-primary mx-3" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
            See all
          </button>
        </div>
        
        <div class="liked-movie-img-box d-flex justify-content-center align-items-center">
          <div v-for=" (movie,index) in slicedMovieList" :key="index" class="liked-movie-img mx-3" :id="`movie-${index}`">
            <!-- 클릭하면 영화 상세페이지로 가게 하기 -->
            <img :src="poster_path + movie.poster_path" alt="" class="movie-img" @click="goToDetail(movie)">
          </div>
        </div>
      </div>
    </div>

    <!-- Modal For liked Movies -->
    <div>
      <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
          <div class="modal-dialog liked-movie-modal-dialog modal-lg">
            <div class="modal-content liked-movie-modal-content">
              <div class="modal-header">
                <h5 class="modal-title liked-movie-p" id="staticBackdropLabel">Liked Movies</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <div class="container-fluid">
                  <div class="row row-cols-4">
                    <img class="modal-img my-3" @click="goToDetail(movie)" data-bs-dismiss="modal" :src="poster_path + movie.poster_path" alt="" v-for="movie, idx in profile.movie_likes" :key="idx">
                  </div>
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
    </div>

    
      <!-- 작성한 글 -->
    <h2>작성한 글</h2>
    <ul>
      <li v-for="article in profile.articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 글</h2>
    <ul>
      <li v-for="article in profile.like_articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  components: {

  },
  data : function() {
    return{
      poster_path: 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/',
    }
  },
  computed: {
    ...mapGetters(['profile']),
    slicedMovieList: function() {
      const reversedList = [...this.profile.movie_likes].reverse()
      return reversedList.slice(0,8)
    },
    slicedActorList: function() {
      return this.profile.actor_counts
    }
  },
  methods: {
    ...mapActions(['fetchProfile']),
    goToDetail: function(movieData) {
      console.log(movieData)
      this.$router.push({name: 'movieDetail', params: { movieId: movieData.movie_id, movie: movieData}})
    },
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    
  },
}
</script>

<style>
.for-nav{
  height: 5em;
}

h1{
  color: rgba(240,240,240,1);
}

.liked-movie-box {
  /* width: 45em; */
  height: 24em;
  border-radius: 0.8em;
}

.liked-movie-img-box{
  width: 100%;
  height: 60%;
  background: rgb(10,10,10);
  border-radius: 1em;
}

.liked-movie-img {

  position: relative;
}
/* .liked-movie-img:not(#movie-0, #movie-1) {
  right: 5em;
}
#movie-1 {

  right: 2.5em;
} */
.movie-img {
  width: 100%;
  border-radius: 0.5em;
}

.movie-img:hover {
  opacity: 50%;
}

.liked-movie-modal-content{
  background: rgba(30,30,30,1);
}
.modal-img {
  border-radius: 1em;
}
.liked-movie-p{
  color: rgba(240,240,240,1);
}
</style>