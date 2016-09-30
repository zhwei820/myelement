<style media="screen">
  #app, body, html {
    height: 100%;
    margin: 0;
  }
  .full {
    height: 100%;
  }
  .side_bar {
    background-color: #eff2f7;
    height: 100%;
  }

</style>

<template>
  <div id="app">

    <!-- <el-menu theme="dark" default-active="1" class="el-menu-demo" mode="horizontal" >
      <img src="./assets/logo.png" width="60px">
    </el-menu> -->
    <my-header></my-header>

    <el-row class="full">
      <el-col :span="3" class="side_bar">
        <sidebar-menu></sidebar-menu>
      </el-col>

      <el-col :span="18">

        <router-view></router-view>

      </el-col>
    </el-row>

  </div>
</template>

<script>

// import MainHeader from './header.vue';
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
