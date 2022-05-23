import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

export default{
  state: {

  },
  getters: {

  },
  mutations: {

  },
  actions: {
    writeReview: function({getters}, credentials) {
      axios({
        method:'post',
        url: drf.articles.writeReview(credentials.movie_id),
        data: credentials,
        headers: getters.authHeader
      })
        .then(() =>
          router.push({name: 'movieDetail', params: { movieId: credentials.movie_id,}})
        )
    }
  },
}