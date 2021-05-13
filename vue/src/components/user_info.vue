<template>
  <div>
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
                  <span class="number">1,252</span>
                  <span class="title">累計賣出成本</span>
              </p>
            </div>
          </div>
          <div class="col-md-3">
            <div class="metric">
              <span class="icon"><i class="fa fa-shopping-bag"></i></span>
              <p>
                <span class="number">203</span>
                <span class="title">累計售出金額</span>
              </p>
            </div>
          </div>
          <div class="col-md-3">
          <div class="metric">
            <span class="icon"><i class="fa fa-eye"></i></span>
            <p>
              <span class="number">274,678</span>
              <span class="title">累計獲利</span>
            </p>
            </div>
          </div>
          <div class="col-md-3">
            <div class="metric">
              <span class="icon"><i class="fa fa-bar-chart"></i></span>
              <p>
                <span class="number">35%</span>
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
          <tbody align="center">
            <tr>
              <td><a href="#">763648</a></td>
              <td>Steve</td>
              <td>$122</td>
              <td>Oct 21, 2016</td>
              <td><span class="label label-success">COMPLETED</span></td>
            </tr>
          </tbody>
          <tfoot align="center">
            <tr>
              <th>Total</th>
              <th rowspan="1" colspan="2">總持有股票數量: 22</th>
              <th rowspan="1" colspan="1">總持有股票成本: 22000</th>
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
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <fieldset class="form-group">
              <div class="row">
                <legend class="col-form-label col-sm-3 pt-0">交易動作</legend>
                <div class="col-sm-8">
                  <div class="form-check" v-for="(item, index) in activity_list">
                    <input class="form-check-input" type="radio" :name="'activity' + (index)" id="'activity' + (index)" :value="item" v-model="form.activity">
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
                         :disabled="form.activity == ''" v-if="form.activity != 'Sell'" @change="onchange_stock_symbol()" v-model="form.stock_symbol">
                  <select class="form-control" name="stock_symbol" id="stock_symbol" placeholder="股票代號"
                          v-if="form.activity == 'Sell'" v-model="form.stock_symbol">
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
                         v-model="form.stock_name" v-validate="{required: true}">
                  <span class="warning_word" v-if="errors.first('stock_name')">{{ errors.first('stock_name') }}</span>
                </div>
              </div>
              <div class="form-group row">
                <label for="price" class="col-sm-3 col-form-label">交易單價</label>
                <div class="col-sm-8">
                  <input class="form-control" id="price" name="price"
                         v-model="form.price" placeholder="交易單價" v-validate="{required: true, integer: true}" @blur="calculate_total_cost()">
                  <span class="warning_word" v-if="errors.first('price')">{{ errors.first('price') }}</span>
                </div>
              </div>
              <div class="form-group row">
                <label for="volume" class="col-sm-3 col-form-label">交易股數</label>
                <div class="col-sm-8">
                  <input class="form-control" id="volume" name="volume" placeholder="交易股數"
                         v-model="form.volume" v-validate="{required: true, integer: true}" @blur="calculate_total_cost()">
                  <span class="warning_word" v-if="errors.first('volume')">{{ errors.first('volume') }}</span>
                </div>
              </div>
              <div class="form-group row" v-if="form.activity == 'Sell'">
                <label for="cost" class="col-sm-3 col-form-label">交易成本</label>
                <div class="col-sm-8">
                  <input class="form-control" id="cost" v-model="form.cost" placeholder="交易成本" readonly>
                </div>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <h2 class="h2_padding" v-if="form.price != 0 & form.volume != 0">成交金額: {{ total_cost }}</h2>
            <button type="button" class="btn btn-secondary" data-dismiss="modal">No</button>
            <button type="button" class="btn btn-primary" data-dismiss="modal" @click="sign_out()">Yes</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'HelloWorld',
    data () {
      return {
        activity_list: ['Buy', 'Sell'],
        stock_symbol_list: ['2330', '2335'],
        total_cost: 0,
        form: {
          stock_symbol: '',
          stock_name: '',
          activity: '',
          volume: 0,
          price: 0,
          cost: 0
        }
      }
    },
    created: function () {
        // Connect API
        var google_token = this.get_cookie('google_token')
        axios({
            method: 'get',
            url: 'http://www.stockhelper.com.tw:8889/api/users',
            params: { 'google_token': google_token}
        })
        .then(function (response) {
            console.log(response);
            if (response.data['login_status'] === 0) {
                // 轉頁
                 location.href = response.data['url']
            }
        })
        .catch(function (error) {
            console.log(error);
        })
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
                  integer: '請輸入數字。'
                },
                price: {
                  required: '請輸入單價。',
                  integer: '請輸入數字。'
                }
            }
        };
        this.$validator.localize('en', dict);
    },
    methods: {
        get_cookie: function (name) {
            var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
            if (match) return match[2];
        },
        onchange_stock_symbol: function () {
          const vuex_store = this.$store
          parent.this = this
          // Connect API
          axios({
              method: 'post',
              url: 'http://www.stockhelper.com.tw:8889/api/stock_basic_info',
              data: {
                user_email: vuex_store.getters.user_email,
                stock_symbol: this.form.stock_symbol,
                activity: this.form.activity,
              }
          })
          .then(function (response) {
              console.log(response);
              parent.this.form.stock_name = response.data
          })
          .catch(function (error) {
              console.log(error);
          })
        },
        calculate_total_cost: function () {
          console.log(this.form.price)
          this.total_cost = this.form.price * this.form.volume
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src="@/assets/user_info/css/user_info.css">


</style>
