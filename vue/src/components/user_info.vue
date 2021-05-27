<template>
  <div>
    <breadcrumb></breadcrumb>
    <div class="panel panel-headline">
      <div class="panel-heading">
          <h3 class="panel-title">Quickly Overview</h3>
      </div>
      <div class="panel-body">
        <div class="row">
          <div class="col-md-3">
            <div class="metric">
              <span class="icon"><i class="fa fa-download"></i></span>
              <p>
                  <span class="number">{{ page_info.quick_review_info.total_cost | currency(0) | money }}</span>
                  <span class="title">累計賣出成本</span>
              </p>
            </div>
          </div>
          <div class="col-md-3">
            <div class="metric">
              <span class="icon"><i class="fa fa-shopping-bag"></i></span>
              <p>
                <span class="number">{{ page_info.quick_review_info.total_sell | currency(0) | money }}</span>
                <span class="title">累計售出金額</span>
              </p>
            </div>
          </div>
          <div class="col-md-3">
          <div class="metric">
            <span class="icon"><i class="fa fa-eye"></i></span>
            <p>
              <span class="number">{{ page_info.quick_review_info.total_profit | currency(0) | money }}</span>
              <span class="title">累計獲利</span>
            </p>
            </div>
          </div>
          <div class="col-md-3">
            <div class="metric">
              <span class="icon"><i class="fa fa-bar-chart"></i></span>
              <p>
                <span class="number">{{ page_info.quick_review_info.profit_percent }}</span>
                <span class="title">獲利率</span>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 庫存資料 -->
    <div class="panel panel-headline">
      <div class="panel-heading">
        <h3 class="panel-title">庫存資料</h3>
      </div>
      <div class="panel-body no-padding">
        <table class="table table-striped">
          <thead align="center">
            <tr>
              <th>股票代號</th>
              <th>股票名稱</th>
              <th>持有股數</th>
              <th>持有成本</th>
              <th>更新時間</th>
            </tr>
          </thead>
          <tbody align="center" v-for="(item, index) in page_info.inventory_list">
            <tr>
              <td><a href="#">{{ item.stock_symbol }}</a></td>
              <td>{{ item.stock_name }}</td>
              <td>{{ item.on_hand_volume | currency(0) }}</td>
              <td>{{ item.cost | currency(2) | money }}</td>
              <td><span class="label label-success">{{ item.updated_at }}</span></td>
            </tr>
          </tbody>
          <tfoot align="center">
            <tr>
              <th>Total</th>
              <th rowspan="1" colspan="2">總持有股票數量: {{ page_info.inventory_count | currency}}</th>
              <th rowspan="1" colspan="1">總持有股票成本: {{ page_info.total_inventory_cost | currency | money  }}</th>
              <th rowspan="1" colspan="1"><div class="col-md-3 text-right"><a href="#" class="btn btn-primary" data-toggle="modal" data-target="#CreateTrade">執行交易</a></div></th>
            </tr>
          </tfoot>
        </table>
      </div>
      <div class="panel-footer">
      </div>
    </div>
    <!-- Modal -->
    <modal></modal>
  </div>
</template>

<script>
import Modal from './modal'
import Breadcrumb from './breadcrumb'
export default {
  name: 'user_info',
  components: {
    Modal,
    Breadcrumb
  },
  data () {
    return {
      page_info: {
        quick_review_info: '',
        total_inventory_cost: '',
        inventory_count: '',
        inventory_list: ''
      },
    }
    },
    created: function () {
      // Connect API
      this.get_page_info()
    },
    filters:{
      currency(value, digits) {
        const number_obj = parseFloat(value)
        const output = number_obj.toFixed(digits).replace(/\d(?=(\d{3})+\.)/g, '$&,')
        return output
      },
      money(value) {
        const parts = value.toString().split('.');
        parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
        return '$' + parts.join('.');
      },
    },
    methods: {
        get_cookie: function (name) {
            var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
            if (match) return match[2];
        },
        get_page_info: function() {
          const google_token = this.get_cookie('google_token')
          if (google_token === undefined) {
            this.$router.push({ name: 'Login'})
          }
          const parent_this = this
          axios({
            method: 'get',
            url: 'http://www.stockhelper.com.tw:8889/api/stock_basic_info',
            params: {'google_token': google_token}
          })
          .then(function (response) {
            console.log(response.data)
            parent_this.page_info = response.data
          })
          .catch(function (error) {
            alert('請登入。')
            console.log(error);
            parent_this.$router.push({ name: 'Login'})
          })
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src="@/assets/user_info/css/user_info.css">


</style>
