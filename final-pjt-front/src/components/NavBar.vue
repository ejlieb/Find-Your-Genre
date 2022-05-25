<template>
  <nav class="navbar navbar-expand-lg fixed-top">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <img src="@/assets/My_project.png" alt="" @click= "gotoHome" class="ms-3 me-auto logo">

      <div class="dropdown me-2 ">
        <input class="form-control dropdown-toggle" type="search" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false" :value="searchData" @input="changeKeyword"> 
        <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1" v-show="searchData !== ''" >
          <li v-for="search, idx in searchList" :key="idx" class="d-flex align-items-center search-item dropdown-item" @click="goToDetail(search)" >
            <img :src="path + search.poster_path" alt="" class="search-img me-2">
            <a href="#" style="text-decoration: none;">{{ search.title }}</a>
          </li>
        </ul>
      </div>


      <!-- <div class="d-flex mx-5" role="search">
        <input class="form-control me-2 dropdown-toggle" type="search" id="dropdownMenuButton1"  data-bs-toggle="dropdown" aria-expanded="false" placeholder="Search" aria-label="Search" :value="searchData" @input="changeKeyword">
      </div> -->


      <ul class="navbar-nav mb-2 mb-lg-0 me-3">
        <li class="nav-item nav-route mx-1" v-if="isLoggedIn">
          <router-link :to="{name: 'profile', params: { username } }" class="nav-route">Profile</router-link>
        </li>
        <li class="nav-item nav-route mx-1" v-if="!isLoggedIn">
          <router-link :to="{name: 'signup'}" class="nav-route">SignUp</router-link>
        </li>
        <li class="nav-item nav-route mx-1" v-if="isLoggedIn">
          <router-link :to="{name: 'logout' }" class="nav-route">Logout</router-link>
        </li>
        <li v-if="!isLoggedIn" class="nav-item nav-route mx-1">
          <router-link :to="{ name: 'signin' }" class="nav-route">Login</router-link>
        </li>
        <!-- <li class="nav-item nav-route mx-1" @click="goBack">
          Back
        </li> -->
      </ul>
      


    </div>
  </div>
</nav>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'NavBar',
  data: function() {
    return {
      searchData: '',
      path: 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2/',
    }
  },
  methods: {
    gotoHome: function() {
      this.$router.push({ name: 'home'})
    },
    sendSearchRequest: function() {
      this.$store.dispatch("sendSearchRequest", this.searchData )
    },
    goToDetail: function(movieData) {
      console.log(movieData)
      this.$router.push({name: 'movieDetail', params: { movieId: movieData.movie_id, movie: movieData}})
    },
    changeKeyword: function(word) {
      this.searchData = word.target.value
      this.sendSearchRequest()
    },
    goBack: function() {
      this.$router.go(-1)
    }
    },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser', 'searchList']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    },
  },

}
</script>

<style>
  .logo{
    width:10rem;
  }
  img:hover{
    cursor: pointer;
  }
  nav{
    height: 5em;
  }
  .search-img {
    height: 5em;
  }
  .search-item {
    border-color: grey;
  }
  .nav-route {
    color: rgba(240, 240, 240, 1)
  }
</style>