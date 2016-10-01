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
  <div class="side-bar">

  <div class="side-bar__header">
    <div class="site-name">
    	<a href="./"><img src="/dist/logo.png"><span>Adminize</span></a>
    </div>
  </div>


    <div class="scroll-wrap">
  	<div class="scroll-content">
  		<ul class="side-bar__menu">
  			<li class="side-bar__list">
  			<div class="parent-title js-side-parent is-open">
  				<i class="fa fa-flag icon"></i><span>Getting Started</span>
  			</div>
  			<ul class="child-menu" style="display: block;">
  				<li class="child-menu__list"><router-link to="/">Install</router-link> </li>
  				<li class="child-menu__list"><router-link to="/111">template</router-link> </li>
  			</ul>
  			</li>
  			<li class="side-bar__list">
  			<div class="parent-title js-side-parent">
  				<i class="fa fa-star icon"></i><span>Basics</span>
  			</div>
  			<ul class="child-menu">
  				<li class="child-menu__list"><router-link to="/00001">Install1</router-link> </li>
  				<li class="child-menu__list"><router-link to="/00002">Install2</router-link> </li>
  				<li class="child-menu__list"><router-link to="/00003">Install3</router-link> </li>
  				<li class="child-menu__list"><router-link to="/00004">Install4</router-link></li>
  				<li class="child-menu__list"><router-link to="/00005">Install5</router-link></li>
  				<li class="child-menu__list"><router-link to="/00006">Install6</router-link></li>
  				<li class="child-menu__list"><router-link to="/00007">Install7</router-link></li>
  			</ul>
  			</li>
  			<li class="side-bar__list">
  			<div class="parent-title js-side-parent">
  				<i class="fa fa-cubes icon"></i><span>Components</span>
  			</div>
  			<ul class="child-menu">
  				<li class="child-menu__list"><router-link to="/0000g">Installq</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000q">Installw</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000w">Installe</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000e">Installr</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000r">Installt</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000t">Instally</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000y">Installu</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000u">Installi</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000i">Installo</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000o">Installg</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000f">Installj</router-link></li>
  				<li class="child-menu__list"><router-link to="/0000s">Installk</router-link> </li>
  			</ul>
  			</li>
  		</ul>
  	</div>
  </div>


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

    }
  }

</script>
