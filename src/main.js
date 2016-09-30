







// import entry from './app';

import Vue from 'vue'
import VueRouter from 'vue-router';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import App from './app.vue';


import bodyTest from './pages/bodyTest.vue';


Vue.use(ElementUI);
Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'hash',
  base: __dirname,
  routes: [
    { path: '/', component: bodyTest },
    { path: '/foo', component: bodyTest },
    { path: '/bar', component: bodyTest }
  ]
});

new Vue({ // eslint-disable-line
  render: h => h(App),
  router
}).$mount('#app');


// router.start(App, '#app');
