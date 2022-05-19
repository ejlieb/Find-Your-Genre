<template>
  <!-- <nav class="fixed-top d-flex align-items-center justify-content-between">
      <img src="@/assets/My_project.png" alt="" @click= "gotoHome">
      <div>
        <router-link to="/">Home</router-link> |
        <router-link :to="{name: 'genre', params: {genreId : 20} }">Genre</router-link>|
        <router-link :to="{name: 'profile', params: {profileId : 20} }">Profile</router-link>|
        <router-link :to="{name: 'signup'}">SignUp</router-link>
      </div>
      
  </nav> -->
  <nav class="navbar navbar-expand-lg fixed-top">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
      <img src="@/assets/My_project.png" alt="" @click= "gotoHome" class="ms-3 me-auto">
      <ul class="navbar-nav mb-2 mb-lg-0 me-3">
        <li class="nav-item">
          <router-link :to="{name: 'profile', params: {profileId : 20} }">Profile</router-link>|
        </li>
        <li class="nav-item">
          <router-link :to="{name: 'signup'}">SignUp</router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>
</template>

<script>
export default {
  name: 'NavBar',
  methods: {
    gotoHome: function() {
      this.$router.push({ name: 'home'})
    }
  }
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