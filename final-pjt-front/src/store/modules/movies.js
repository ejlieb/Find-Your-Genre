
import axios from 'axios'
import drf from '@/api/drf'


export default {
  state: {
    movieForChoose : [],
    movieForHome : [],
    searchList: [],
    movieDetail: {},
    movieForGenreMain: [],
  },
  getters: {
    movieForChoose: state => state.movieForChoose,
    movieForHome: state => state.movieForHome,
    searchList: state => state.searchList,
    movieDetail: state => state.movieDetail,
    movieForGenreMain: state => state.movieForGenreMain,
  },
  mutations: {
    setMovieForChoose: function (state, movieList) {
      state.movieForChoose = movieList
    },
    setMovieForHome: function(state, movieList) {
      state.movieForHome = movieList
    },
    setMovieForGenreMain: function(state, movieList){
      state.movieForGenreMain = movieList
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
    // 홈화면 영화 캐러젤 정보
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

    // 장르 영화 화면 캐러젤 정보
    getMovieForGenreMain: function( { commit, getters }, genreId) {
      const axiosObject = {
        method: 'get',
        url: drf.movies.genreMainMovies(genreId),
      }
      if (getters.isLoggedIn) {
        axiosObject.headers = getters.authHeader
      }

      axios(axiosObject)
        .then(res => {
          commit('setMovieForGenreMain', res.data)
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



