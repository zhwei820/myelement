<style media="screen">

</style>

<template>
  <div id="app">

    <el-menu theme="dark" default-active="1" class="el-menu-demo" mode="horizontal" >
      <img src="./assets/logo.png" width="60px">
    </el-menu>

    <el-row class="full">
      <el-col :span="3" class="side_bar">
        <!-- <sidebar-menu></sidebar-menu> -->
      </el-col>

      <el-col :span="18">

        <table-edit></table-edit>
      </el-col>
    </el-row>

  </div>
</template>

<script>

import tableEdit from "./tableEdit.vue";

export default {
  data () {
    return {

    }
  },
  components:{
    tableEdit: tableEdit,
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
