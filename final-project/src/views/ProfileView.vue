<template>
  <div class="profile">
    <h1>This is an {{ $route.params.profileId }} page</h1>
    <profile-info></profile-info>
    <my-movie></my-movie>
  </div>
</template>

<script>
import MyMovie from '../components/MyMovie.vue'
import ProfileInfo from '../components/ProfileInfo.vue'
export default {
  components: { ProfileInfo, MyMovie },
  name: 'ProfileView',

}
</script>

<style>
  .profile{
    height: 4000px;
  }
</style>