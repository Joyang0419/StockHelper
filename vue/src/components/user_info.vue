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
                  <span class="number">{{ page_info.quick_review_info.total_cost }}</span>
                  <span class="title">累計賣出成本</span>
              </p>
            </div>
          </div>
          <div class="col-md-3">
            <div class="metric">
              <span class="icon"><i class="fa fa-shopping-bag"></i></span>
              <p>
                <span class="number">{{ page_info.quick_review_info.total_sell }}</span>
                <span class="title">累計售出金額</span>
              </p>
            </div>
          </div>
          <div class="col-md-3">
          <div class="metric">
            <span class="icon"><i class="fa fa-eye"></i></span>
            <p>
              <span class="number">{{ page_info.quick_review_info.total_profit }}</span>
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
              <td>{{ item.on_hand_volume }}</td>
              <td>{{ item.cost }}</td>
              <td><span class="label label-success">{{ item.updated_at }}</span></td>
            </tr>
          </tbody>
          <tfoot align="center">
            <tr>
              <th>Total</th>
              <th rowspan="1" colspan="2">總持有股票數量: {{ page_info.inventory_count }}</th>
              <th rowspan="1" colspan="1">總持有股票成本: {{ page_info.total_inventory_cost }}</th>
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
      user_email: '',
      activity_list: ['Buy', 'Sell'],
      stock_symbol_list: [],
      activity: '',
      stock_symbol: '',
      stock_name: '',
      on_hand_volume: 0,
      total_cost: 0,
      total_profit: 0,
      page_info: {
        quick_review_info: '',
        total_inventory_cost: '',
        inventory_count: '',
        inventory_list: ''
      },
      form: {
        stock_basic_info_id: '',
        volume: 0,
        price: 0,
        cost: 0
      },
    }
    },
    created: function () {
      // Connect API
      this.get_page_info()
      // vee-validate custom words
      const dict = {
      custom: {
              stock_symbol: {
                  required: '請輸入股票代號。',
              },
              stock_name: {
                required: '股票代號有誤。'
              },
              volume: {
                required: '請輸入交易量。',
                integer: '請輸入數字。',
                max_value: '交易股數要<=持有股數。',
                min_value: '交易股數至少1股。'
              },
              price: {
                required: '請輸入單價。',
                decimal: '請輸入數字。'
              },
          }
      };
      this.$validator.localize('en', dict);
    },
    methods: {
        get_cookie: function (name) {
            var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
            if (match) return match[2];
        },
        onchange_stock_activity: function () {
          // 交易動作: sell，向後端索取可販售的證卷代號。
          if (this.activity == 'Buy') {
            return true
          }
          parent.this = this
          // Connect API
          axios({
              method: 'post',
              url: 'http://www.stockhelper.com.tw:8889/api/stock_basic_info',
              data: {
                action: 'get_stock_symbol_list',
                user_email: this.user_email,
              }
          })
          .then(function (response) {
              console.log(response);
              parent.this.stock_symbol_list = response.data
          })
          .catch(function (error) {
              console.log(error);
          })
        },
        onchange_stock_symbol: function () {
          parent.this = this
          // Connect API
          axios({
              method: 'post',
              url: 'http://www.stockhelper.com.tw:8889/api/stock_basic_info',
              data: {
                action: 'get_stock_name',
                activity: this.activity,
                user_email: this.user_email,
                stock_symbol: this.stock_symbol,
              }
          })
          .then(function (response) {
              console.log(response);
              parent.this.stock_name = response.data['stock_name']
              parent.this.form.cost = response.data['cost']
              parent.this.form.stock_basic_info_id = response.data['stock_basic_info_id']
              parent.this.on_hand_volume = response.data['sell_stock_volume']
          })
          .catch(function (error) {
              console.log(error);
          })
        },
        calculate_total_cost: function () {
          this.total_cost = this.form.price * this.form.volume
          this.total_profit = (parseInt(this.form.price) - parseInt(this.form.cost)) * parseInt(this.form.volume)
        },
        checkForm: function() {
        // 檢查表單
          this.$validator.validate().then(valid => {
						if (valid) {
              this.submitForm()
              $('#CreateTrade').modal('hide')
              this.reset_data()
              return true
            }
            // 滑到error的地方
            document.getElementById(this.$validator.errors.items[0].field).scrollIntoView(false);
            return true
					});
				},
        submitForm: function() {
        // 提交表單
          if (this.activity === 'Buy') {
            this.form.cost = this.form.price
          }
          if (this.activity === 'Sell') {
            this.form.volume = - (this.form.volume)
          }
          console.log(this.form)
          axios({
            method: 'post',
            url: 'http://www.stockhelper.com.tw:8889/api/stock_basic_info',
            data: {
              action: 'submit',
              user_email: this.user_email,
              form: this.form,
            }
          })
          .then(function (response) {
            alert(response.data)
            location.href = './'
          })
          .catch(function (error) {
              console.log(error);
          })
        },
        reset_data: function() {
            Object.assign(this.$data, this.$options.data());
            this.user_email = this.$store.getters.user_email
            this.get_page_info()
        },
        get_page_info: function() {
          var google_token = this.get_cookie('google_token')
          var vuex_store = this.$store
          if (google_token === undefined) {
            location.href = './login'
          }
          parent.this = this
          axios({
            method: 'get',
            url: 'http://www.stockhelper.com.tw:8889/api/stock_basic_info',
            params: {'google_token': google_token}
          })
          .then(function (response) {
            if (response.data['login_status'] === 0) {
              // 轉頁
              location.href = response.data['url']
            }
            parent.this.user_email = vuex_store.getters.user_email
            parent.this.page_info = response.data
          })
          .catch(function (error) {
            console.log(error);
          })
        },
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src="@/assets/user_info/css/user_info.css">


</style>
