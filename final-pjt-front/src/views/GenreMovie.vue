<template>
<div class="home">
  <genre-movie-main :key="componentKey"></genre-movie-main>
</div>
</template>

<script>
import GenreMovieMain from '../components/GenreMovieMain.vue'
// @ is an alias to /src

export default {
  name: 'GenreMovie',
  components: {
    GenreMovieMain
  },
  data() { return { componentKey: 0, }; }, 
  methods: { forceRerender() { this.componentKey += 1; } } 

  
}
</script>

<style>
  .home {
  }
  
</style>
