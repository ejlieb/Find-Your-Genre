<template>
  <div class="home-main">
    <div class="for-nav"></div>
    <button @click="test">click</button>
    <p>{{ homeMainMovies }}</p>
    <div class="main-box">
      <div class="movie-title">
        <span style="font-size: 5em;">Movie Title</span>
      </div>
      <div class="movie-overview">
        <span>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Architecto, rerum. Sed dicta, ipsam aliquid illo mollitia omnis incidunt amet ratione corrupti aperiam consectetur, recusandae quam optio ducimus minima natus rerum. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Architecto, rerum. Sed dicta, ipsam aliquid illo mollitia omnis incidunt amet ratione corrupti aperiam consectetur, recusandae quam optio ducimus minima natus rerum. </span>
        <div class="movie-info">
        <!-- 장르 버튼에 v-for= "" key="#"넣기 -->
        <button type="button" class="btn btn-outline-light mx-2">Genre</button> 
        <button type="button" class="btn btn-outline-light mx-2">8.0</button> 
          <div class="movie-add">
          <!-- v-on click통해 디테일페이지로 라우트 / 영화 좋아요하기 -->
          <button type="button" class="btn btn-danger mx-2">Detail</button>
          <button type="button" class="btn btn-outline-light mx-2">Add To Watchlist</button> 
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeMain",
  // mounted: function() {
  //     this.$store.dispatch('getMovieForHome')
  //   },
  computed: {
      homeMainMovies: function() {
        return this.$store.getters.movieForHome
      }
    },
  methods: {
    test: function() {
      this.$store.dispatch('getMovieForHome')
    }
  }
}
</script>

<style>
.home-main {
  height:60em;
  background:linear-gradient(0deg, rgba(0,0,0,0.8), rgba(100, 100, 100, 0.2)), url('https://www.themoviedb.org/t/p/original/6RuU7NumrO08Bcml5sIgj9zNWFm.jpg');
  overflow: hidden;
}
.home-img {
  width: 100%;
}
.for-nav{
  height: 5em;
}
.main-box{
  height: 55em;
}
.movie-title{
  font:'';
  position: absolute;
  top: 13em;
  left: 10em;
  color: rgba(240,240,240,1);
}
.movie-overview
{
  width: 30%;
  font:'';
  position: absolute;
  top: 20.5em;
  left: 10em;
  color: rgba(240,240,240,1);
  text-align: left;

}
.movie-info{
  font:'';
  position: relative;
  top: 2em;
  color: rgba(240,240,240,1)
}
.movie-add{
  font:'';
  position: relative;
  top: 2em;
  color: rgba(240,240,240,1)
}
</style>