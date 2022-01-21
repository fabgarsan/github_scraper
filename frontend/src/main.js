import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import {BFormDatepicker} from 'bootstrap-vue';

Vue.component('BFormDatepicker', BFormDatepicker)

new Vue({
  render: h => h(App),
}).$mount('#app')
