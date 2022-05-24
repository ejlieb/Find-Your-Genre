import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default{
  state: {
    reviewDetail: {},
  },
  getters: {
    reviewDetail: state => state.reviewDetail
  },
  mutations: {
    setReviewDetail: function(state, review) {
      console.log(review)
      state.reviewDetail = review
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
    }

  },
}