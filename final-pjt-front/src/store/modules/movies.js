
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    movieForChoose : [],
    movieForHome : [],
    serachList: [],
  },
  getters: {
    movieForChoose: state => state.movieForChoose,
    movieForHome: state => state.movieForHome,
    searchList: state => state.searchList,
  },
  mutations: {
    setMovieForChoose: function (state, movieList) {
      state.movieForChoose = movieList
    },
    setMovieForHome: function(state, movieList) {
      state.movieForHome = movieList
    },
    setSearchResult: function(state, searchList) {
      state.searchList = searchList
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
    getMovieForHome: function( { commit, getters }) {
      const axiosObject = {
        method: 'get',
        url: drf.movies.homeMainMovies(),
      }
      console.log('hi')
      if (getters.isLoggedIn) {
        axiosObject.headers = getters.authHeader
      }

      axios(axiosObject)
        .then(res => {
          console.log('hi')
          commit('setMovieForHome', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },
    sendSearchRequest: function({ commit }, search) {
      axios({
        method: 'get',
        url: drf.movies.sendSearchRequest(),
        data: search,
      })
        .then(res => {
          commit('setSearchREsult', res.data)
        })
    } 
    
  },
}



