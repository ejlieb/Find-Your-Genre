<template>
<div class="home">
  <home-main :key="componentKey"></home-main>
  <genre-card></genre-card>
</div>
</template>

<script>
import GenreCard from '../components/GenreCard.vue'
import HomeMain from '../components/HomeMain.vue'
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    GenreCard,
    HomeMain
  },
  data() { return { componentKey: 0, }; }, 
  methods: { forceRerender() { this.componentKey += 1; } } 

  
}
</script>

<style>
  .home {
  }
  
</style>


