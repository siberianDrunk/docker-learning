import Vue from 'vue'
import App from './App.vue'
import VueFullPage from 'vue-fullpage.js'

import router from  './router/index.js'


Vue.use(VueFullPage);

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})


