<template>
  <nav class="navbar navbar-expand-lg fixed-top">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <img src="@/assets/My_project.png" alt="" @click= "gotoHome" class="ms-3 me-auto">

      <!-- v-for 작업 마무리하기 -->
      <div class="list-group" v-if="searchData !== ''">
        <div class="list-group-item list-group-item-action" aria-current="true" v-for="search, idx in searchList" :key="idx" @click="goToDetail(search)">
          <div>
            <img src="" alt="">
            <p>{{ search.title }}</p>
          </div>
        </div>
      </div>


      <div class="d-flex mx-5" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="searchData" @keyup="sendSearchRequest">
      </div>


      <ul class="navbar-nav mb-2 mb-lg-0 me-3">
        <li class="nav-item" v-if="isLoggedIn">
          <router-link :to="{name: 'profile', params: { username } }">Profile</router-link>|
        </li>
        <li class="nav-item" v-if="!isLoggedIn">
          <router-link :to="{name: 'signup'}">SignUp</router-link>|
        </li>
        <li class="nav-item" v-if="isLoggedIn">
          <router-link :to="{name: 'logout'}">Logout</router-link>|
        </li>
        <li v-if="!isLoggedIn" class="nav-item">
          <router-link :to="{ name: 'signin' }">Login</router-link>
        </li>
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
      this.$router.push({name: 'movieDetail', params: { movieId: movieData.Id, movieData: movieData }})
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
  img{
    width:10rem;
  }
  img:hover{
    cursor: pointer;
  }
  .list-group{
    position: relative;
    top: 8.5em;
    left: 17em;
    width: 30em;
  }
  nav{
    height: 5em;
  }
</style>