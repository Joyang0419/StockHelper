import Vue from 'vue'
import Router from 'vue-router'
import UserInfo from '@/components/user_info'
import Login from '@/components/login'

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
  ]
})
