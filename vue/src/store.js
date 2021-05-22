import Vue from 'vue';

Vue.use(Vuex);

// 定義一個新的 Vue Store

export default new Vuex.Store({
// 狀態，template需要用到的值
  state: {
    username: '匿名用戶',
    user_image_url: '',
    user_email: '',
  },
// 取的state的值
  getters: {
    username: function (state) {
      return state.username
    },
    user_image_url: function (state) {
      return state.user_image_url
    },
    user_email: function (state) {
      return state.user_email
    },
  },
// 寫method
  mutations: {
    update_username(state, username) {
      state.username = username
    },
    update_user_image_url(state, user_image_url) {
      state.user_image_url = user_image_url
    },
    update_user_email(state, user_email) {
      state.user_email = user_email
    },
  },
// 執行mutations方法，給store.dispatch
  actions: {
    update_user_info(context, data) {
      context.commit('update_username', data['username'])
      context.commit('update_user_image_url', data['user_image_url'])
      context.commit('update_user_email', data['user_email'])
    },
  }
})

