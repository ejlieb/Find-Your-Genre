<template>
  <div>
    <div class="for-nav" style="height: 5em;"></div>
    <div class="for-nav" style="height: 5em;"></div>
    <div class="container">
      <div class="row">
        <div class="col-4 poster-box">
          <img :src="path + detail.poster_path" alt="" class="poster">
        </div>
        <div class="col detail d-flex flex-column">
          <!-- 영화 상세정보 -->
          <div class="title align-self-start d-flex" >
            <h1>{{detail.title}}</h1>
            <button type="button" class="btn btn-outline-light mx-2" @click="writeReview(detail.movie_id  )">Write Review</button>
          </div>
          <div class="botton-box d-flex justify-contetn-start my-2">
            <button type="button" class="btn btn-outline-light mx-2" v-for="genre, idx in detail.genres" :key="idx">{{ genre.genre_name }}</button> 
            <button type="button" class="btn btn-outline-light mx-2">{{detail.vote_average}}</button>
          </div>
          <div class="overview aligh-self-start my-2">
            <p class="text-start">{{detail.overview}}</p>
          </div>
        </div>
      </div>
      <h1>Casting</h1>
      <div class="row p-3 g-3">
        <div class="card border-secondary col mx-2" style="width: 18rem; background:rgb(15,15,15);" v-for="actor in detail.actors" :key="actor.actor_id">
          <img class="card-img-top mt-2" :src="path + actor.profile_path" alt="Card image cap">
          <div class="card-body">
            <p class="card-text">{{ actor.name }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieDetail",
  created: function () {
    this.$store.dispatch('sendDetailRequest', this.movieId)
  },
  // beforeRouteUpdate(to, from, next){
  //   console.log('next')
  //   this.$store.dispatch('sendDetailRequest', this.movie.movie_id)
  //   console.log(this.movie)
  //   next()
  // },
  data: function() {
    return {
      movie: this.$route.params.movie,
      movieId: this.$route.params.movieId,
      path: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/',
    }
  },
  computed:  {
    detail: function() {
      return this.$store.getters.movieDetail
    }
  },
  methods: {
    writeReview: function(id) {
      this.$router.push({name: 'writeReview', params: {movieId: id}})
    }
  }
}
</script>

<style>
  .row {
    height: 40em;
  }
  .poster{
    height: 80%;
    width: auto;
  }
  .poster-box{
    height: 100%;
  }
</style>