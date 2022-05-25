<template>
  <div class="container">

    <!-- <h1>{{topTenList}}</h1> --> -->
    <div class="top-ten-carousel d-flex flex-column align-items-start my-5">
      <h1 class="mx-3">TOP 10</h1>
      <div id="carouselExampleControls" class="carousel slide row container" data-bs-ride="carousel">
        <div class="carousel-inner row">
          <div class="carousel-item active">
            <div class=" row row-cols-5 g-4 ">
              <div class="col topten-item" v-for="topTen, idx in topTenList.slice(0,5)" :key="idx" >
                <div class="topten-item" :style="`background-image: url(${ poster_path + topTen.poster_path }); background-size: cover; background-position: center;`"></div>
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class=" row row-cols-5 g-4 ">
              <div class="col topten-item" v-for="topTen, idx in topTenList.slice(5,10)" :key="idx" >
                <div class="topten-item" :style="`background-image: url(${ poster_path + topTen.poster_path }); background-size: cover; background-position: center;`"></div>
              </div>
            </div>
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>
      
      
    <div class="test"></div>

    
  </div>
</template>

<script>
export default {
  name: 'GenreRecommendation',
  data: function() {
    return {
       poster_path: 'https://image.tmdb.org/t/p/w600_and_h900_bestv2/',

    }
  },
  created: function() {
    this.$store.dispatch('getRecommendation', this.$route.params.genreId)
  },
  computed: {
    topTenList: function() {
      return this.$store.getters.topTen
    }
  }
}
</script>

<style>
  .topten-item {
    height: 25em;
  }
</style>