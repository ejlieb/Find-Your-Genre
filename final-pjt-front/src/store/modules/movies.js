
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    movieForChoose : [],
    movieForHome : [],
  },
  getters: {
    movieForChoose: state => state.movieForChoose,
    movieForHome: state => state.movieForHome,
  },
  mutations: {
    setMovieForChoose: function (state, movieList) {
      state.movieForChoose = movieList
    },
    setMovieForHome: function(state, movieList) {
      state.movieForHome = movieList
    }
  },
  actions: {
    getMovieForChoose: function( { commit } ) {
      axios({
        method: 'get',
        url: drf.movies.chooseMovies(),
      })
        .then(res => {
          commit('setMovieForChoose', res.data)
        })
    },
    getMovieForHome: function( { commit }) {
      axios({
        method: 'get',
        url: drf.movies.homeMainMovies()
      })
        .then(res => {
          commit('setMovieForHome', res.data)
        })
    } 
  },
}



