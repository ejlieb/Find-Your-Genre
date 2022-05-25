<template>
  <div>
    <div class="for-nav" style="height: 5em;"></div>
    <div class="for-nav" style="height: 5em;"></div>
    <div class="container">
      <div class="row poster-row">
        <div class="col-4 poster-box">
          <img :src="path + detail.poster_path" alt="" class="poster" @click="goToDetail(detail)">
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
            <button type="button" class="btn btn-danger mx-2" @click="updateReview" v-if="currentUser.pk === review.user.pk">Update</button>
            <button type="button" class="btn btn-danger mx-2" @click="deleteReview" v-if="currentUser.pk === review.user.pk">Delete</button>
          </div>
          <div class="d-flex">
            <button type="button" class="mt-1 mx-1 btn btn-outline-light rating-btn">{{review.rating}}</button>
            <button type="button" class="mt-1 mx-1 btn btn-outline-light rating-btn" @click="likeReview">{{review.good_eval_count}}</button>
            <button type="button" class="mt-1 mx-1 btn btn-outline-light rating-btn" @click="badReview">{{review.bad_eval_count}}</button> 
          </div>
          <div class="d-flex mt-5">
            <p>{{review.content}}</p>
          </div>
        </div>
      </div>

      <div>
        <form @submit.prevent="commentCreate">
        <label for="inputPassword5" class="form-label">Password</label>
        <div class="d-flex">
          <input type="text" id="inputPassword5" class="form-control" @input="changeKeyword">
          <button type="submit">submit</button>
        </div>
        </form>  
      </div>
      <ol class="list-group list-group-numbered">
        <li class="list-group-item d-flex justify-content-between align-items-start" v-for="comment, idx in commentList" :key="idx">
          <div class="ms-2 me-auto">
            <div class="fw-bold">Username</div>
            {{comment.content}}
          </div>
          <span class="badge bg-primary rounded-pill" @click="deleteComment(comment)">delete</span>
        </li>
      </ol>
      <div>
        <p>{{ commentList }}</p>
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
    this.$store.dispatch('getCommentList', this.commentPack)
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
        reviewId: this.$route.params.reviewPk
        },
      content: '',
      commentPack: {
        movieId: this.$route.params.movieId, 
        reviewId: this.$route.params.reviewPk,
        content: ''
      }
    }
  },
  computed:  {
    detail: function() {
      return this.$store.getters.movieDetail
    },
    review: function() {
      return this.$store.getters.reviewDetail
    },
    currentUser: function() {
      return this.$store.getters.currentUser
    },
    commentList: function() {
      return this.$store.getters.commentList
    }
  },
  methods: {
    updateReview: function() {
      this.$router.push({name: 'updateReview', params: {movieId: this.idPack.movieId, reviewId : this.idPack.reviewId, title: this.review.title, content: this.review.content, rating: this.review.rating}})
    },
    gotoReview: function(movieId, reviewId){
      this.$router.push({name: 'reviewView', params: {movieId: movieId,reviewPk: reviewId }})
    },
    likeReview: function() {
      this.$store.dispatch('sendReviewLikeRequest', this.idPack)
    },
    goToDetail: function(movieData) {
      this.$router.push({name: 'movieDetail', params: { movieId: movieData.movie_id, movie: movieData}})
    },
    badReview: function() {
      this.$store.dispatch('sendReviewBadRequest', this.idPack)
    },
    deleteReview: function() {
      this.$store.dispatch('deleteReview', this.idPack)
    },
    changeKeyword: function(event) {
      this.content = event.target.value
    },
    commentCreate: function() {
      this.commentPack.content = this.content
      this.$store.dispatch('createComment', this.commentPack)
      this.comment =''
    },
    deleteComment: function(comment) {
      const deletePack = {
        reviewId: this.$route.params.reviewPk,
        commentId: comment.id
      }
      this.$store.dispatch('deleteComment', deletePack, this.commentPack)
    }

    // 잘라내기 해서 리뷰 작성페이지로 보내기

  },
  watch: {
    review(val){
      this.review.good_eval_count = val.good_eval_count
      this.review.bad_eval_count = val.bad_eval_count
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