<template>
  <div>
    <div class="for-nav" style="height: 5em;"></div>
    <div class="container">
      <div class="row">
        <img src="" alt="">
        <div class="detail">
          <!-- 영화 상세정보 -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieDetail",
  data: function() {
    return {
      movie: this.$route.params.movieData
    }
  }
}
</script>

<style>

</style>