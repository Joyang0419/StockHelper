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
                  <div class="form-check">
                    <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios1" value="option1" checked>
                    <label class="form-check-label" for="gridRadios1">
                      買進
                    </label>
                  </div>
                  <div class="form-check disabled">
                    <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios3" value="option3">
                    <label class="form-check-label" for="gridRadios3">
                      賣出
                    </label>
                  </div>
                </div>
              </div>
            </fieldset>
            <form>
              <div class="form-group row">
                <label for="inputEmail3" class="col-sm-3 col-form-label">股票代號</label>
                <div class="col-sm-8">
                  <input type="email" class="form-control" id="inputEmail3" placeholder="股票代號">
                </div>
              </div>
              <div class="form-group row">
                <label for="inputPassword3" class="col-sm-3 col-form-label">股票名稱</label>
                <div class="col-sm-8">
                  <input class="form-control" id="inputPassword3" placeholder="股票名稱" disabled>
                </div>
              </div>
              <div class="form-group row">
                <label for="inputPassword3" class="col-sm-3 col-form-label">交易單價</label>
                <div class="col-sm-8">
                  <input class="form-control" id="inputPassword3" placeholder="交易單價">
                </div>
              </div>
              <div class="form-group row">
                <label for="inputPassword3" class="col-sm-3 col-form-label">交易股數</label>
                <div class="col-sm-8">
                  <input class="form-control" id="inputPassword3" placeholder="交易股數">
                </div>
              </div>
              <div class="form-group row">
                <label for="inputPassword3" class="col-sm-3 col-form-label">交易成本</label>
                <div class="col-sm-8">
                  <input class="form-control" id="inputPassword3" placeholder="交易股數">
                </div>
              </div>
            </form>
          </div>
          <div class="modal-footer">
            <h2 class="h2_padding">成交金額: 123</h2>
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
        msg: 'Welcome to Your Vue.js App',
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
    },
    methods: {
        get_cookie: function (name) {
            var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
            if (match) return match[2];
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped src="@/assets/user_info/css/user_info.css">


</style>
