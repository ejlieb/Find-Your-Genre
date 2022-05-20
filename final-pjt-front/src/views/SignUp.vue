<template>
  <div class="sign-up">
    <div class="for-nav"></div>
    <div class="sign-up-form ">
      <h1>Signup</h1>

      <account-error-list v-if="authError"></account-error-list>

      <form @submit.prevent="signup(credentials)">
        <div>
          <label for="username">Username: </label>
          <input  v-model="credentials.username" type="text" id="username" required/>
        </div>
        <div>
          <label for="password1">Password: </label>
          <input v-model="credentials.password1" type="password" id="password1" required />
        </div>
        <div>
          <label for="password2">Password Confirmation:</label>
          <input v-model="credentials.password2" type="password" id="password2" required />
        </div>
        <div>
          <button>Signup</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  // import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignUp',
    // components: {
    //   AccountErrorList,
    // },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style>
.sign-up{

}
.for-nav{
  height: 5em;
}
  
  </style>