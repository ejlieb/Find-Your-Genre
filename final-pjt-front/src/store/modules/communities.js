import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default{
  state: {
    reviewDetail: {},
    genreReviews : [],
  },
  getters: {
    reviewDetail: state => state.reviewDetail,
    genreReviews: state => state.genreReviews,
  },
  mutations: {
    setReviewDetail: function(state, review) {
      console.log(review)
      state.reviewDetail = review
    },
    setGenreReviews: function(state, reviews) {
      state.genreReviews = reviews
    }
  },
  actions: {
    writeReview: function({getters}, credentials) {
      axios({
        method:'post',
        url: drf.communities.writeReview(credentials.movie_id),
        data: credentials,
        headers: getters.authHeader
      })
        .then(() =>
          router.push({name: 'movieDetail', params: { movieId: credentials.movie_id,}})
        )
    },
    sendReviewRequest: function({commit}, idPack){
      axios({
        method:'get',
        url: drf.communities.reviewDetail(idPack.reviewId, idPack.movieId)
      })
        .then( function(res) {
          commit('setReviewDetail', res.data)
        }
        
        )
    },
    sendReviewLikeRequest: function({getters, dispatch}, idPack) {
      axios({
        method: 'post',
        url: drf.communities.reviewLike(idPack.reviewId, idPack.movieId),
        headers: getters.authHeader
      })
        .then( () =>
          dispatch('sendReviewRequest', idPack)
        )
    },
    sendReviewBadRequest: function({getters, dispatch}, idPack) {
      axios({
        method: 'post',
        url: drf.communities.reviewBad(idPack.reviewId, idPack.movieId),
        headers: getters.authHeader
      })
        .then( () =>
          dispatch('sendReviewRequest', idPack)
        )
    },
    getReviews: function({commit}, genreId){
      axios({
        method: 'get',
        url: drf.communities.genreReviews(genreId)
      })
        .then((res) =>
          commit('setGenreReviews', res.data)
        )
    },
    updateReview: function({getters}, credentials) {
      axios({
        method:'put',
        url: drf.communities.updateReview(credentials.review_id, credentials.movie_id),
        data: credentials,
        headers: getters.authHeader
      })
        .then(() =>
          router.push({name: 'reviewView', params: { movieId: credentials.movie_id, reviewPk: credentials.review_id}})
        )
    },
    deleteReview: function({getters}, idPack) {
      axios({
        method: 'delete',
        url: drf.communities.updateReview(idPack.reviewId, idPack.movieId),
        headers: getters.authHeader,
      })
      .then(() =>
      router.push({name:'home'})
      )
    }

  },
}