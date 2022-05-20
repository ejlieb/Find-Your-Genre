<template>
  <div>
    <h1>{{ profile.username }}</h1>
    <!-- <h1>{{ profile}}</h1> -->
    <div class="liked-movie-box d-flex flex-column">
      <p class="liked-movie-p align-self-start mb-4">Liked Movies</p>
      <div class="liked-movie-img-box d-flex justify-content-center">
        <div v-for=" (movie,index) in slicedMovieList" :key="index" class="liked-movie-img" :id="`movie-${index}`">
          <img :src="poster_path + movie.poster_path" alt="" class="movie-img">
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
      return this.profile.movie_likes.slice(0,5)
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
h1{
  color: rgba(240,240,240,1);
}

.liked-movie-box {
  width: 45em;
  height: 20em;
  background:linear-gradient(0deg, rgba(250,250,250,0.4), rgba(250, 250, 250, 0.2))
}

.liked-movie-img-box{
  width: 100%;
  height: 70%;
  background: black;
}

.liked-movie-img {
  height: 70%;
  width: 20%;
}
.liked-movie-img:not(#movie-0, #movie-1) {
  position: relative;
  right: 5em;
}
#movie-1 {
  position: relative;
  right: 2.5em;
}
.movie-img {
  width: 100%;
}
</style>