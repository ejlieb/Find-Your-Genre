<template>
  <div>
    <h1>{{ profile.username }}</h1>
    <h1>{{ profile.movie_likes[1].poster_path}}</h1>
  </div>
</template>

<script>
export default {
  name: 'ProfileInfo',

}
</script>

<style>

</style>