import Vue from 'vue'
import Router from 'vue-router'
import UserInfo from '@/components/user_info'
import Login from '@/components/login'
import StockData from '@/components/stock_data'
import PageNotFound from '@/components/page_not_found'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'UserInfo',
      component: UserInfo
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/stockData',
      name: 'StockData',
      component: StockData
    },
    {
      path: '*',
      name: 'PageNotFound',
      component: PageNotFound
    },

  ]
})
