<template>
  <div>
    <div class="for-nav" style="height: 5em;"></div>
    <div class="for-nav" style="height: 5em;"></div>
    <div class="container">
      <div class="row poster-row">
        <div class="col-4 poster-box">
          <img :src="path + detail.poster_path" alt="" class="poster">
          <div class="title align-self-start d-flex flex-column align-items-center" >
            <p>{{detail.title}}</p>
            <div class="botton-box d-flex justify-contetn-start my-2">
              <button type="button" class="btn btn-outline-light mx-2" v-for="genre, idx in detail.genres" :key="idx">{{ genre.genre_name }}</button> 
            </div>
          </div>
        </div>
        <div class="col detail d-flex flex-column">
          <!-- 영화 상세정보 -->
          
          <div class="d-flex review-title aligh-self-start mt-5">
            <h1 class="text-start">{{review.title}}</h1>
            <button type="button" class="btn btn-outline-light mx-2 like-btn" @click="likeReview">Like</button> 
          </div>
          <div class="d-flex">
            <button type="button" class="mt-1 mx-1 btn btn-outline-light rating-btn">{{review.rating}}</button>
            <button type="button" class="mt-1 mx-1 btn btn-outline-light rating-btn">{{review.user_good_eval.length}}</button>
            <button type="button" class="mt-1 mx-1 btn btn-outline-light rating-btn">{{review.user_bad_eval.length}}</button> 
          </div>
          <div class="d-flex mt-5">
            <p>{{review.content}}</p>
            <p>{{review}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewView",
  created: function () {
    this.$store.dispatch('sendDetailRequest', this.movieId)
    this.$store.dispatch('sendReviewRequest', this.idPack)
  },
  // beforeRouteUpdate(to, from, next){
  //   console.log('next')
  //   this.$store.dispatch('sendDetailRequest', this.movie.movie_id)
  //   console.log(this.movie)
  //   next()
  // },
  data: function() {
    return {
      // movie: this.$route.params.movie,
      movieId: this.$route.params.movieId,
      path: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/',
      reviewId: this.$route.params.reviewPk,
      idPack: {
        movieId: this.$route.params.movieId, 
        reviewId: this.$route.params.reviewPk}
    }
  },
  computed:  {
    detail: function() {
      return this.$store.getters.movieDetail
    },
    review: function() {
      return this.$store.getters.reviewDetail
    }
  },
  methods: {
    writeReview: function(id) {
      this.$router.push({name: 'writeReview', params: {movieId: id}})
    },
    gotoReview: function(movieId, reviewId){
      this.$router.push({name: 'reviewView', params: {movieId: movieId,reviewPk: reviewId }})
    },
    likeReview: function() {
      this.$store.dispatch('sendReviewLikeRequest', this.idPack)
    }
  }
}
</script>

<style>
  .poster-row {
    height: 40em;
  }
  .poster{
    height: 80%;
    width: auto;
  }
  .poster-box{
    height: 100%;
  }
  .like-btn{
    height: 80%;
  }

</style>