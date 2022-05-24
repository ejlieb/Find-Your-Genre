<template>
  <div class="container">
    <h1>{{genreReviews}}</h1>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div class="col-3"  v-for="review, idx in genreReviews" :key="idx">
        <div class="card">
          <img src="#" class="card-img-top" alt="...">
          <div class="card-body">
            <h5 class="card-title">{{review.title}}</h5>
            <p class="card-text">{{review.rating}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommunityView',
  data: function() {
    return {
      genreId: this.$route.params.genreId
    }
  },
  created: function() {
    this.$store.dispatch("getReviews", this.genreId)
  },
  computed: {
    genreReviews: function() {
      return this.$store.getters.genreReviews
    }
  }
}
</script>

<style>

</style>