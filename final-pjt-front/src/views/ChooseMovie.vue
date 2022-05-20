<template>
  <div>
    <div class="for-nav"></div>
    <div class="choose-movie-container container">
      <p id="instruction" >{{ this.$route.params.username }}님 재미있게 봤던, 혹은 보고싶은 영화를 10개 이상 골라주세요!</p>
      <p>{{ choosedMovieList }} </p>
      <p v-if="choosedMovie.length < 10">아직 {{ 10 - choosedMovie.length }}개의 영화를 더 고르셔야 합니다.</p>
      <div v-else>
        <p>다음 단계로 넘어가세요! {{choosedMovieList.length }}개의 영화를 고르셨습니다!</p>
        <button type="button" class="btn btn-primary" @click="saveLikes" >회원 가입 완료하기</button>
      </div>
      <div class="row mt-5">
        <!-- div에 v-for 돌리기 키값으로 title div에 id 줘서 숨겼다 보였다-->
        <div class="poster-card col-2" v-for="movie in movieList" :key="movie.movie_id" @mouseover="showTitle(movie.movie_id)" @mouseout="hideTitle(movie.movie_id)" @click="addMovie(movie.movie_id)" :id="`movieselected-${movie.movie_id}`">
          <img :src="poster_path + movie.poster_path" alt="" class="card-img">
          <div class="card-title d-flex flex-column justify-content-center hide" :id="`movie-${movie.movie_id}`" >
            <p>{{ movie.title}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import drf from '@/api/drf'
export default {
  name: 'ChooseMovie',
  data: function() {
    return {
      poster_path: 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/',
      choosedMovie: [],
      test: null,
      data: {
        username: this.$route.params.username,
        likeMovieIds: [],
      }
      
    }
  },
  computed: {
    movieList: function() {
      return this.$store.getters.movieForChoose
    },
    choosedMovieList: function() {
      return this.choosedMovie
    }
    
  },

  beforeMount: function() {
      this.$store.dispatch('getMovieForChoose')
    },

  methods: {
    showTitle: function(id) {
      let target = this.$el.querySelector(`#movie-${id}`)
      target.classList.add('show')
      target.classList.remove('hide')
    },
    hideTitle: function(id) {
      let target = document.querySelector(`#movie-${id}`)
      console.log(target)
      target.classList.add('hide')
      target.classList.remove('show')
    },
    addMovie: function(id) {
      if (this.choosedMovie.includes(id) === false) {
          this.choosedMovie.push(id)
          let target = this.$el.querySelector(`#movieselected-${id}`)
          target.setAttribute('style', 'opacity:10%;')
      }
      else {
        this.choosedMovie = this.choosedMovie.filter( function(ele){
          return ele !== id
        })
        let target = this.$el.querySelector(`#movieselected-${id}`)
        target.setAttribute('style', 'opacity:100%;')
      }
      
    },
    saveLikes: function() {
      this.data.likeMovieIds = this.choosedMovie
      axios({
        method: 'post',
        url: drf.accounts.saveLikes(),
        data: this.data
      })
      .then(
        this.$router.push({ name: 'home' })
      )
    }
  }
}
</script>

<style>
  #instruction {
    font-size : 2em;
  }
  .choose-movie-container {
    position: relative;
    top: 5em;
  }
  .card-img {
    width: 100%;
  }
  .card-img:hover {
    opacity: 50%;
  }
  .card-title {
    position: relative;
    bottom: 10em;
    max-width: 100%;
  }
  .card-title:hover{
    cursor: pointer;
  }
  .show {
    visibility: visible;
  }
  .hide {
    visibility: hidden;
  }
</style>