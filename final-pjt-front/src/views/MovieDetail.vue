<template>
  <div>
    <div class="for-nav" style="height: 5em;"></div>
    <div class="for-nav" style="height: 5em;"></div>
    <div class="container">
      <div class="row">
        <div class="col-4 poster-box">
          <img :src="path + movie.poster_path" alt="" class="poster">
        </div>
        <div class="col detail d-flex flex-column">
          <!-- 영화 상세정보 -->
          <div class="title align-self-start">
            <h1>{{movie.title}}</h1>
          </div>
          <div class="overview aligh-self-start">
            <p>{{movie.overview}}</p>
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
    this.$store.dispatch('sendDetailRequest', this.movie.movie_id)
  },
  data: function() {
    return {
      movie: this.$route.params.movie,
      path: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/',
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