import Vue from 'vue'
import Router from 'vue-router'
import UserInfo from '@/components/user_info'
import Login from '@/components/login'
import StockData from '@/components/stock_data'
import PageNotFound from '@/components/page_not_found'
import AI_Predict from '@/components/ai_predict'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'UserInfo',
      component: UserInfo,
      meta: {
        breadcrumb: [
          {
            name: '首頁',
            path: '/'
          },
          {
            name: '使用者庫存',
            path: '/'
          }
        ]
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/stockData',
      name: 'StockData',
      component: StockData,
      meta: {
        breadcrumb: [
          {
            name: '首頁',
            path: '/'
          },
          {
            name: '個股資訊',
            path: '/stockData'
          }
        ]
      }
    },
    {
      path: '/aipredict',
      name: 'AI_Predict',
      component: AI_Predict,
      meta: {
        breadcrumb: [
          {
            name: '首頁',
            path: '/'
          },
          {
            name: '智能預測',
            path: '/aipredict'
          }
        ]
      }
    },
    {
      path: '*',
      name: 'PageNotFound',
      component: PageNotFound
    },
  ]
})
