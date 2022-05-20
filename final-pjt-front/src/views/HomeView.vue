<template>
<div class="home">
  <home-main></home-main>
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
  
}
</script>

<style>
  .home {
  }
  
</style>


