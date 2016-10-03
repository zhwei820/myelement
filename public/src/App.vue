<style media="screen">
  .height_100 {
    height: 100%;
  }
</style>

<template>

  <div id="app" class="height_100">
    <div v-if='user_data.logged_in'>
      <my-header v-on:_logged_out="do_logout"></my-header>
      <sidebar-menu></sidebar-menu>

      <div class="main-contents">
        <div class="main-contents__body">
          <router-view></router-view>
        </div>
      </div>
    </div>
    <div v-else='user_data.logged_in' class="height_100" >
      <login v-on:_logged_in="do_login" :user_data='user_data'></login>

    </div>

  </div>
</template>

<script>

import sidebarMenu from './layout/sidebar-menu.vue';
import myHeader from './layout/header.vue';
import login from './pages/login.vue';

var user_info = localStorage.getItem('user');
export default {
  data () {
    return {
      user_data: (user_info && user_info != 'undefined' ? JSON.parse(user_info) : {
        logged_in: false,
      })

    }
  },
  components:{
    sidebarMenu: sidebarMenu,
    myHeader: myHeader,
    login: login,

  },
  methods: {
    do_login(user_data) {
      this.user_data = user_data;
      localStorage.setItem('user', JSON.stringify(this.user_data))
      location.href = '/'
    },
    do_logout() {
      this.user_data.logged_in = false;
      localStorage.setItem('user', JSON.stringify(this.user_data))
    },

  }
}

</script>

<style>
body {
  font-family: Helvetica, sans-serif;
}
</style>
