<style media="screen">
  .height_100 {
    height: 100%;
  }
</style>

<template lang="html">

<div class="page-login height_100" >
  <div class="login">
    <div class="login__head">
      <h1 class="login__title"><i class="fa fa-sign-in"></i><span>Sign in to Dashboard</span></h1></div>
    <div class="login__body">
      <form class="" action="/" method="post">

        <el-alert v-if="error_message"
          :title="error_message"
          type="warning">
        </el-alert>
        <div class="login__list"><label for="name" class="login__label">用户名</label><input type="email" v-model="user.email" placeholder="email" class="input--full" autocomplete="on"></div>
        <div class="login__list"><label for="password" class="login__label">密码</label><input type="password" v-model="user.password" placeholder="Password"  class="input--full" autocomplete="on"></div>
        <div class="login__list"><label for="password" class="login__label">验证码</label><input type="text" v-model="user.code" placeholder="" class="input--full"> <img src="/ends/a_user/code/?a" onclick="this.src=this.src + '&' + Math.random()"></img> </div>

      </form>

    </div>
    <div class="login__foot">
      <ul class="list-btn align--center" >
        <li><a href="#" class="btn btn--success" @click.prevent="login">登录</a></li>
      </ul>
    </div>
  </div>

</div>

</template>

<script>

export default {
  data () {
    return {
      user: {
        email: this.user_data && this.user_data.email,
        password: this.user_data && this.user_data.password,
        code: '',
      },
      error_message: '',
    }
  },
  props: ['user_data'],
  computed: {},
  mounted () {
    console.log(this.user_data);
  },
  methods: {
    login(a, e) {
      this.$http.post('/ends/a_user/login/', this.user, {params: this.user}).then((response) => {
        if(response.data.status > 0){
          this.error_message = response.data.message;
        }else {
          this.$emit('_logged_in', response.data.data);
        }
    });

      // this.$notify({
      //   title: 'It Works',
      //   message: 'We have laid the groundwork for you. Now it\'s your time to build something epic!',
      //   duration: 6000
      // })
    },

  },
  components: {
  }
};
</script>

<style lang="css">
</style>
