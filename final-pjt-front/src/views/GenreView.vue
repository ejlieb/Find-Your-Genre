<template>
  <div :class="{'sf': this.genreId === 2, 'horror': this.genreId === 1}">
    <div class="for-nav"></div>

    <h1 :class="{'sf-title': this.genreId === 2,}" class="">This is an {{ $route.params.genreId }} page</h1>
    <div :class="{'sf-title': this.genreId === 2,}" class="main-box">
      <div class="movie-title">
        <span style="font-size: 5em;" v-if="this.genreId === 2">SF / FANTASY</span>
      </div>
      <div class="movie-overview">
        <span v-if="this.genreId === 2">Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa, eos. Cum eaque, nemo explicabo, fugit distinctio nesciunt dolore temporibus, dignissimos ut accusamus soluta blanditiis maiores libero voluptatum numquam quae pariatur?</span>
      </div>
    </div>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
</template>


<script>
export default {
  name: 'GenreView',
  data: function() {
    return {
      genreId : this.$route.params.genreId,
    }
  }
}
</script>

<style>
  .for-nav{
  height: 5em;
}
/* 장르별 클래스 */
.horror{
  height: 100vh;
  background:linear-gradient(0deg, rgba(0,0,0,1), rgba(255, 255, 255, 0.1)), url('@/assets/Horror.png');
  background-size: cover;
}
  .sf{
    height: 100vh;
    background:linear-gradient(0deg, rgba(0,0,0,1), rgba(255, 255, 255, 0.1)), url('@/assets/SF.jpg');
    background-size: cover;
  }
  .sf-title{
    font-family: 'Odibee Sans', cursive;
  }
</style>