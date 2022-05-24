<template>
  <div :class="{'sf': this.genreId === 2, 'horror': this.genreId === 1, 'anime': this.genreId === 3, 'action': this.genreId === 4, 'drama': this.genreId === 5, 'docu': this.genreId === 6, 'comedy': this.genreId === 7}">
    <div class="for-nav"></div>


    <div :class="{'sf-title': this.genreId === 2, 'horror-title': this.genreId === 1, 'anime-title': this.genreId === 3, 'action-title': this.genreId === 4, 'drama-title': this.genreId === 5, 'docu-title': this.genreId === 6,'comedy-title': this.genreId === 7 }" class="main-box" >
      <div class="movie-title">
        <span style="font-size: 5em;" v-if="this.genreId === 1">HORROR / THRILLER </span>
        <span style="font-size: 5em;" v-if="this.genreId === 2">SF / FANTASY</span>
        <span style="font-size: 5em;" v-if="this.genreId === 3">ANIMATION</span>
        <span style="font-size: 5em;" v-if="this.genreId === 4">action</span>
        <span style="font-size: 5em;" v-if="this.genreId === 5">DRAMA / ROMANCE</span>
        <span style="font-size: 5em;" v-if="this.genreId === 6">DOCUMENTARY / HISTORY</span>
        <span style="font-size: 5em;" v-if="this.genreId === 7">코미디</span>

      </div>
      <div class="movie-overview">
        <span v-if="this.genreId === 1">Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa, eos. Cum eaque, nemo explicabo, fugit distinctio nesciunt dolore temporibus, dignissimos ut accusamus soluta blanditiis maiores libero voluptatum numquam quae pariatur?</span>
        <span v-if="this.genreId === 2">Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa, eos. Cum eaque, nemo explicabo, fugit distinctio nesciunt dolore temporibus, dignissimos ut accusamus soluta blanditiis maiores libero voluptatum numquam quae pariatur?</span>
        <span v-if="this.genreId === 3">Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa, eos. Cum eaque, nemo explicabo, fugit distinctio nesciunt dolore temporibus, dignissimos ut accusamus soluta blanditiis maiores libero voluptatum numquam quae pariatur?</span>
        <span v-if="this.genreId === 4">Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa, eos. Cum eaque, nemo explicabo, fugit distinctio nesciunt dolore temporibus, dignissimos ut accusamus soluta blanditiis maiores libero voluptatum numquam quae pariatur?</span>
        <span v-if="this.genreId === 5">Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa, eos. Cum eaque, nemo explicabo, fugit distinctio nesciunt dolore temporibus, dignissimos ut accusamus soluta blanditiis maiores libero voluptatum numquam quae pariatur?</span>
        <span v-if="this.genreId === 6">Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa, eos. Cum eaque, nemo explicabo, fugit distinctio nesciunt dolore temporibus, dignissimos ut accusamus soluta blanditiis maiores libero voluptatum numquam quae pariatur?</span>
        <span v-if="this.genreId === 7">Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa, eos. Cum eaque, nemo explicabo, fugit distinctio nesciunt dolore temporibus, dignissimos ut accusamus soluta blanditiis maiores libero voluptatum numquam quae pariatur?</span>



      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-slide="prev" @click="goToGenreCommunity">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-slide="next" @click="goToGenreMovie">
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
  },
  methods: {
    goToGenreMovie: function() {
      console.log('장르로간다')
      this.$router.push({name: 'genreMovie', params: {movieId: this.genreId}})
    },
    goToGenreCommunity: function() {
      this.$router.push({name: 'genreCommunity', params: {genreId: this.genreId}})
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
    background:linear-gradient(0deg, rgba(0,0,0,1), rgba(0, 0, 0, 0.3)), url('@/assets/Horror.png');
    background-size: cover;
}
  .sf{
    height: 100vh;
    background:linear-gradient(0deg, rgba(0,0,0,1), rgba(255, 255, 255, 0.1)), url('@/assets/SF.jpg');
    background-size: cover;
 }
  .anime{
    height: 100vh;
    background:linear-gradient(0deg, rgba(0,0,0,1), rgba(255, 255, 255, 0.1)), url('@/assets/Anime.jpg');
    background-size: cover;
}
  .action{
    height: 100vh;
    background:linear-gradient(0deg, rgba(0,0,0,1), rgba(255, 255, 255, 0.1)), url('@/assets/Action.png');
    background-size: cover;
  }
  .drama{
    height: 100vh;
    background:linear-gradient(0deg, rgba(0,0,0,1), rgba(255, 255, 255, 0.1)), url('@/assets/Drama.jpg');
    background-size: cover;
  }
  .docu{
    height: 100vh;
    background:linear-gradient(0deg, rgba(0,0,0,1), rgba(0, 0, 0, 0.2)), url('@/assets/Documentary.jpg');
    background-size: cover;
  }
  .comedy{
    height: 100vh;
    background:linear-gradient(0deg, rgba(0,0,0,1), rgba(0, 0, 0, 0.2)), url('@/assets/Comedy.jpg');
    background-size: cover;
  }
  /* 장르별 폰트 클래스 */
  .horror-title{
    font-family: 'Fredericka the Great', cursive;
  }
  .sf-title{
    font-family: 'Odibee Sans', cursive;
  }
  .anime-title {
    font-family: 'Audiowide', cursive;
  }
  .action-title{
    font-family: 'skyfall';
  }
  .drama-title {
    font-family: 'Ruthie', cursive;
  }
  .comedy-title{
    font-family:'궁서';
  }
  @font-face{
    font-family: 'skyfall';
    src: url('@/assets/fonts/SkyFall Done.ttf')
  }
</style>