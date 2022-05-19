
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    movieForChoose : []
  },
  getters: {
    movieForChoose: state => state.movieForChoose
  },
  mutations: {
    setMovieForChoose: function (state, movieList) {
      state.movieForChoose = movieList
    }
  },
  actions: {
    getMovieForChoose: function( { commit } ) {
      axios({
        method: 'get',
        url: drf.movies.chooseMovies(),
      })
        .then(res => {
          console.log(res)
          commit('setMovieForChoose', res.data)
        })
    }
  },
}



