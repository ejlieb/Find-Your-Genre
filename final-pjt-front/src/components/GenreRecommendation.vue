<template>
  <div class="container">
    <!-- <h1>{{topTenList}}</h1> -->
    <div class="row row-cols-5 g-4">
      <div class="col topten-item" v-for="topTen, idx in topTenList" :key="idx" >
        <div class="topten-item" :style="`background-image: url(${ topTen.movieimage_set[0].image_URL }); background-size: cover; background-position: center;`"></div>
      </div>
    </div>
    <div class="test"></div>
  </div>
</template>

<script>
export default {
  name: 'GenreRecommendation',
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
    height: 30em;
  }
</style>