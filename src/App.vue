

<template>


  <div id="app">
  <my-header></my-header>
  <sidebar-menu></sidebar-menu>

  <div class="main-contents">
    <div class="main-contents__body">
      <router-view></router-view>
    </div>
  </div>

  </div>
</template>

<script>

import sidebarMenu from './layout/sidebar-menu.vue';
import myHeader from './layout/header.vue';

export default {
  data () {
    return {

    }
  },
  components:{
    sidebarMenu: sidebarMenu,
    myHeader: myHeader,
  },
  methods: {

    }
}
</script>

<style>
body {
  font-family: Helvetica, sans-serif;
}
</style>
