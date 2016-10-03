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
    	<a href="./"><img src="dist/logo.png"><span>Adminize</span></a>
    </div>
  </div>

    <div class="scroll-wrap">
  	<div class="scroll-content">
  		<ul class="side-bar__menu">

  			<li class="side-bar__list" v-for="item in menus">
          <div class="parent-title js-side-parent">
            <i class="fa fa-star icon"></i><span>{{ item.name }}</span>
          </div>
          <ul class="child-menu">
            <li class="child-menu__list" v-for="menu in item.sub">
              <router-link :to="menu.route_url">{{ menu.name }}</router-link>
            </li>

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
        menus: [],
        items: ['111', '2222', '44444'],

      }
    },
    methods: {

    },
    mounted() {
      this.$http.get('/ends/a_user/get_menus/').then((response) => {
        console.log(response.data);
        this.menus = response.data
    });

    }
  }

</script>
