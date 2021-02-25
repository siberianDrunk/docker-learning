import Vue from 'vue'
import Router from 'vue-router'
import Main from '../components/Main'
import Grade from '../components/Grade'
import QuotesMain from '../components/quotes/QutoesMain'
import InputMain from "../components/addGrades/InputMain";
import StickyMain from "../components/stickyElements/StickyMain";
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/quotes',
      name: 'quotes',
      component: QuotesMain
    },
    {
      path: '/sticky',
      name: 'sticky',
      component: StickyMain
    },
    {
      path: '/input',
      name: 'input',
      component: InputMain
    },
    {
      path: '/grade/:id',
      name: 'grade',
      component: Grade,
    }
  ]
})
