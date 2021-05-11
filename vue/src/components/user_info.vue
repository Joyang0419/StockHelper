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
                              <span class="title">倉庫成本</span>
                          </p>
                      </div>
                  </div>
              <div class="col-md-3">
                  <div class="metric">
                      <span class="icon"><i class="fa fa-shopping-bag"></i></span>
                      <p>
                          <span class="number">203</span>
                          <span class="title">平倉成本</span>
                      </p>
                  </div>
              </div>
            <div class="col-md-3">
                <div class="metric">
                    <span class="icon"><i class="fa fa-eye"></i></span>
                    <p>
                      <span class="number">274,678</span>
                      <span class="title">平倉獲利</span>
                    </p>
                  </div>
            </div>
            <div class="col-md-3">
                <div class="metric">
                    <span class="icon"><i class="fa fa-bar-chart"></i></span>
                    <p>
                      <span class="number">35%</span>
                      <span class="title">平倉獲利率</span>
                    </p>
                </div>
            </div>
        </div>
      </div>
  </div>

  <div class="panel panel-headline">
  <div class="panel-heading">
      <h3 class="panel-title">庫存資料</h3>
  </div>
  <div class="panel-body no-padding">
        <table class="table table-striped">
          <thead>
            <tr>
              <th>股票代號</th>
              <th>股票名稱</th>
              <th>持有股數</th>
              <th>持有成本</th>
              <th>更新時間</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><a href="#">763648</a></td>
              <td>Steve</td>
              <td>$122</td>
              <td>Oct 21, 2016</td>
              <td><span class="label label-success">COMPLETED</span></td>
            </tr>
            <tr>
              <td><a href="#">763649</a></td>
              <td>Amber</td>
              <td>$62</td>
              <td>Oct 21, 2016</td>
              <td><span class="label label-warning">PENDING</span></td>
            </tr>
            <tr>
              <td><a href="#">763650</a></td>
              <td>Michael</td>
              <td>$34</td>
              <td>Oct 18, 2016</td>
              <td><span class="label label-danger">FAILED</span></td>
            </tr>
            <tr>
              <td><a href="#">763651</a></td>
              <td>Roger</td>
              <td>$186</td>
              <td>Oct 17, 2016</td>
              <td><span class="label label-success">SUCCESS</span></td>
            </tr>
            <tr>
              <td><a href="#">763652</a></td>
              <td>Smith</td>
              <td>$362</td>
              <td>Oct 16, 2016</td>
              <td><span class="label label-success">SUCCESS</span></td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="panel-footer">
          <div class="row">
              <div class="col-md-11 text-right"><a href="#" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">執行交易</a></div>
          </div>
      </div>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
              確定要登出嗎?
          </div>
          <div class="modal-footer">
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
