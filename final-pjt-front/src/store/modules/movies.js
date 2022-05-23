
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    movieForChoose : [],
    movieForHome : [],
    searchList: [],
    movieDetail: {},
  },
  getters: {
    movieForChoose: state => state.movieForChoose,
    movieForHome: state => state.movieForHome,
    searchList: state => state.searchList,
    movieDetail: state => state.movieDetail,
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
    },
    setDetailResult: function(state, movieDetail) {
      state.movieDetail = movieDetail
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
        params: {
          search: search
        },
      })
        .then(res => {
          console.log(res)
          commit('setSearchResult', res.data)
        })
    },
    sendDetailRequest: function({ commit }, id) {
      console.log(id)
      axios({
        method: 'get',
        url: drf.movies.sendDetailRequest() + id
      })
        .then(res => {
          commit('setDetailResult', res.data)
        })
    }
    
  },
}



