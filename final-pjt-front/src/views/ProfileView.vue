<template>
  <div class="container">
    <div class="for-nav"></div>
    <div class="profile-box">
      <h1>{{ profile.username }}</h1>
    <!-- <h1>{{ profile}}</h1> -->
    </div>
    
    <div class="row">
      <div class="liked-movie-box d-flex flex-column col-12">
        <p class="liked-movie-p align-self-start mb-4">Liked Movies</p>
        <div class="liked-movie-img-box d-flex justify-content-center align-items-center">
          <div v-for=" (movie,index) in slicedMovieList" :key="index" class="liked-movie-img mx-3" :id="`movie-${index}`">
            <!-- 클릭하면 영화 상세페이지로 가게 하기 -->
            <img :src="poster_path + movie.poster_path" alt="" class="movie-img">
          </div>
        </div>
      </div>
    </div>

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
  data : function() {
    return{
      poster_path: 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/',
    }
  },
  computed: {
    ...mapGetters(['profile']),
    slicedMovieList: function() {
      return this.profile.movie_likes.slice(0,8)
    }
  },
  methods: {
    ...mapActions(['fetchProfile'])
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
  height: 80%;
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
</style>