<template>
  <div id="app">

    <el-menu theme="dark" default-active="1" class="el-menu-demo" mode="horizontal" >
      <img src="./assets/logo.png" width="60px">
    </el-menu>

    <el-row>
      <el-col :span="3">
        <sidebar-menu></sidebar-menu>
      </el-col>
      <el-col :span="18">
        <table-edit></table-edit>

        <router-view></router-view>
        
      </el-col>
    </el-row>

  </div>
</template>

<script>

import tableEdit from "./tableEdit.vue";
// import MainHeader from './header.vue';
import sidebarMenu from './layout/sidebar-menu.vue';

export default {
  data () {
    return {

    }
  },
  components:{
    tableEdit: tableEdit,
    sidebarMenu: sidebarMenu,
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
