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
    <div class="modal fade" id="CreateTrade" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="reset_data() ">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <fieldset class="form-group">
              <div class="row">
                <legend class="col-form-label col-sm-3 pt-0">交易動作</legend>
                <div class="col-sm-8">
                  <div class="form-check" v-for="(item, index) in activity_list">
                    <input class="form-check-input" type="radio"
                           :name="'activity' + (index)" id="'activity' + (index)" :value="item" v-model="activity" @change="onchange_stock_activity()">
                    <label class="form-check-label" :for="'activity' + (index)">
                      {{ item }}
                    </label>
                  </div>
                </div>
              </div>
            </fieldset>
            <form>
              <!-- activity: buy -> 自行輸入股票代號； sell -> 下拉式選單-->
              <div class="form-group row">
                <label for="stock_symbol" class="col-sm-3 col-form-label">股票代號</label>
                <div class="col-sm-8">
                  <input type="text" name="stock_symbol" class="form-control" id="stock_symbol" placeholder="股票代號" v-validate="{required: true}"
                         :readonly="activity == ''" v-if="activity != 'Sell'" @change="onchange_stock_symbol()" v-model="stock_symbol">
                  <select class="form-control" name="stock_symbol" id="stock_symbol" placeholder="股票代號"
                          v-if="activity == 'Sell'" v-model="stock_symbol" @change="onchange_stock_symbol()">
                      <option value="">請選擇賣出股票</option>
                      <option :value="item"  v-for="(item, index) in stock_symbol_list">{{ item }}</option>
                  </select>
                  <span class="warning_word" v-if="errors.first('stock_symbol')">{{ errors.first('stock_symbol') }}</span>
                </div>
              </div>
              <div class="form-group row">
                <label for="stock_name" class="col-sm-3 col-form-label">股票名稱</label>
                <div class="col-sm-8">
                  <input class="form-control" id="stock_name" name="stock_name" placeholder="股票名稱" readonly
                         v-model="stock_name" v-validate="{required: true}">
                  <span class="warning_word" v-if="errors.first('stock_name')">{{ errors.first('stock_name') }}</span>
                </div>
              </div>
              <div class="form-group row">
                <label for="on_hand_volume" class="col-sm-3 col-form-label">持有股數</label>
                <div class="col-sm-8">
                  <input class="form-control" id="on_hand_volume" name="on_hand_volume" placeholder="持有股數"
                         v-model="on_hand_volume" readonly>
                </div>
              </div>
              <div class="form-group row" v-if="activity == 'Sell'">
                <label for="cost" class="col-sm-3 col-form-label">每股成本</label>
                <div class="col-sm-8">
                  <input class="form-control" id="cost" v-model="form.cost" placeholder="交易成本" readonly>
                </div>
              </div>
              <div class="form-group row">
                <label for="price" class="col-sm-3 col-form-label">每股單價</label>
                <div class="col-sm-8">
                  <input class="form-control" id="price" name="price"
                         v-model="form.price" placeholder="交易單價" v-validate="{required: true, decimal: true}" @blur="calculate_total_cost()">
                  <span class="warning_word" v-if="errors.first('price')">{{ errors.first('price') }}</span>
                </div>
              </div>
              <div class="form-group row" v-if="activity == 'Sell'">
                <label for="volume" class="col-sm-3 col-form-label">交易股數</label>
                <div class="col-sm-8">
                  <input class="form-control" id="volume" name="volume" placeholder="交易股數"
                         v-model="form.volume" v-validate="{required: true, integer: true, max_value: on_hand_volume, min_value: 1}" @blur="calculate_total_cost()">
                  <span class="warning_word" v-if="errors.first('volume')">{{ errors.first('volume') }}</span>
                </div>
              </div>
              <div class="form-group row" v-if="activity != 'Sell'">
                <label for="volume" class="col-sm-3 col-form-label">交易股數</label>
                <div class="col-sm-8">
                  <input class="form-control" id="volume" name="volume" placeholder="交易股數"
                         v-model="form.volume" v-validate="{required: true, integer: true, min_value: 1}" @blur="calculate_total_cost()">
                  <span class="warning_word" v-if="errors.first('volume')">{{ errors.first('volume') }}</span>
                </div>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <h3 class="h2_padding" v-if="form.price != 0 & form.volume != 0 & activity =='Buy'">成交金額: {{ total_cost }}</h3>
            <h3 class="h2_padding" v-if="form.price != 0 & form.volume != 0 & activity !='Buy'">損益金額: {{ total_profit }}</h3>
            <button type="button" class="btn btn-secondary" data-dismiss="modal" @click="reset_data()">No</button>
            <button type="button" class="btn btn-primary" @click="checkForm()">Yes</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Breadcrumb from './breadcrumb'
export default {
  name: 'user_info',
  components: {
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
