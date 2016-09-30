<style media="screen">

  .side-nav .nav-item a {
    font-size: 16px;
    color: #5e6d82;
    line-height: 40px;
    height: 40px;
    margin: 0;
    padding: 0;
    text-decoration: none;
    display: block;
    position: relative;
    -webkit-transition: all .3s;
    transition: all .3s
  }

</style>

<template>
  <div class="">
    <el-menu default-active="2" class="el-menu-vertical-demo side-nav" @open="handleopen" @close="handleclose">
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-message"></i>导航一</template>
        <el-menu-item-group title="分组一">
          <el-menu-item index="1-1">选项1</el-menu-item>
          <el-menu-item index="1-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2" >
          <el-menu-item :index=item v-for="item in items" class="nav-item"><a v-bind:href=item>{{ item }}</a> </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
      <el-menu-item index="2"><i class="el-icon-menu"></i>导航二</el-menu-item>
      <el-menu-item index="3"><i class="el-icon-setting"></i>导航三</el-menu-item>
    </el-menu>
  </div>

</template>

<script>

  module.exports = {
    data: function () {
      return {
        menu: this.$parent.$data.menu || [],
        items: ['111', '2222', '44444'],

      }
    },
    methods: {

      handleopen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleclose(key, keyPath) {
        console.log(key, keyPath);
      },
      handleselect(key, keyPath) {
        console.log(key, keyPath);
      },
    }
  }

</script>
