







// import entry from './app';

import Vue from 'vue'
import VueRouter from 'vue-router';
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import App from './app.vue';

const Home = { template: '<div>home</div>' }

Vue.use(ElementUI);
Vue.use(VueRouter);

new Vue({ // eslint-disable-line
  render: h => h(App),
  // router
}).$mount('#app');


// router.start(App, '#app');
