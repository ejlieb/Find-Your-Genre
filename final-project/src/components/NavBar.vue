<template>
  <nav class="navbar navbar-expand-lg fixed-top">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <img src="@/assets/My_project.png" alt="" @click= "gotoHome" class="ms-3 me-auto">


      <ul class="navbar-nav mb-2 mb-lg-0 me-3">
        <li class="nav-item">
          <router-link :to="{name: 'profile', params: { username } }">Profile {{username}}</router-link>|
        </li>
        <li class="nav-item">
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
  methods: {
    gotoHome: function() {
      this.$router.push({ name: 'home'})
    },
    },
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
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
</style>