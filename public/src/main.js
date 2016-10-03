var getCookie = require('./utilities').getCookie;

import Vue from 'vue'
import VueRouter from 'vue-router';
import ElementUI from 'element-ui'

import 'element-ui/lib/theme-default/index.css'
import App from './app.vue';

var VueResource = require('vue-resource');

Vue.use(VueResource);
Vue.use(ElementUI);
Vue.use(VueRouter);
Vue.http.headers.common['X-CSRFToken'] = getCookie('csrftoken');

import bodyTest from './pages/bodyTest.vue';
import banner from './pages/banner.vue';
import user_list from './pages/user_list.vue';
import user_group from './pages/user_group.vue';

const router = new VueRouter({
  mode: 'hash',
  base: __dirname,
  routes: [
    { path: '/', component: bodyTest },
    { path: '/banner_list_index_operation', component: banner },
    { path: '/notification_operation', component: user_list },
    { path: '/channel_stat', component: user_group },

  ]
});

new Vue({ // eslint-disable-line
  render: h => h(App),
  router
}).$mount('#app');


// router.start(App, '#app');
