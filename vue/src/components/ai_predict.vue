<template>
  <div>
    <breadcrumb></breadcrumb>
    <div class="input-group" style="padding-top: 10px; padding-bottom: 20px">
      <input type="search" class="form-control rounded" placeholder="請輸入股票代號" aria-label="Search"
      aria-describedby="search-addon" v-model="stock_symbol"/>
      <button type="button" class="btn btn-outline-primary"  @click="get_data(stock_symbol)">search</button>
    </div>
    <h6>最近交易日: {{ latest_date }}</h6>
    <!-- line chart -->
    <div id="line_chart" style="height: 400px; min-width: 310px;"></div>
    <!-- bar chart -->
    <figure class="highcharts-figure">
      <div class="col-md-12" id="bar_chart"></div>
    </figure>
    <!-- ai_predict -->
    <div class="panel panel-scrolling">
      <div class="panel-heading">
        <h1 class="panel-title" style="text-align:center">AI智能預測</h1>
      </div>
      <div class="panel-body">
        <ul>
          <li>未來五個交易日價格: {{ ai_predict_data.five_days_predict[0] }},
            {{ ai_predict_data.five_days_predict[1] }},
            {{ ai_predict_data.five_days_predict[2] }},
            {{ ai_predict_data.five_days_predict[3] }},
            {{ ai_predict_data.five_days_predict[4] }}。</li>
          <li>明日價格預測
            <ul>
              <li>無動靜: {{ ai_predict_data.three_days_predict['three_days_no_change'] }}</li>
              <li>漲幅3%以內: {{ ai_predict_data.three_days_predict['three_days_increase_one_percent'] }}</li>
              <li>漲幅3%以上: {{ ai_predict_data.three_days_predict['three_days_increase_three_percent'] }}</li>
              <li>跌幅3%以內: {{ ai_predict_data.three_days_predict['three_days_decrease_one_percent'] }}</li>
              <li>跌幅3%以上: {{ ai_predict_data.three_days_predict['three_days_decrease_three_percent'] }}</li>
            </ul>
          </li>
          <div class="button"><a href="#" class="btn btn-success" data-toggle="modal" data-target="#CreateTrade">執行交易</a></div>
        </ul>
      </div>
    </div>
  <modal></modal>
</div>
</template>

<script>
import Modal from './modal'
import Breadcrumb from './breadcrumb'
export default {
  name: "ai_predict",
  components: {
    Breadcrumb,
    Modal
  },
  data() {
    return {
      stock_symbol: '',
      latest_date: '',
      stock_name: '',
      bar_chart_data: '',
      line_chart_data: '',
      ai_predict_data: {
        three_days_predict: '',
        five_days_predict: ''
      }
    }
  },
  created() {
    this.check_login_status()
    this.get_data('0050')
  },
  mounted() {
  },
  methods: {
    get_cookie: function (name) {
      var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
      if (match) return match[2];
    },
    check_login_status() {
      const google_token = this.get_cookie('google_token')
      if (google_token === undefined) {
        alert('請登入。')
        this.$router.push({ name: 'Login'})
      }
    },
    get_data(stock_symbol) {
      const parent_this = this
      axios({
        method: 'get',
        url: 'http://www.stockhelper.com.tw:8889/api/ai_predict',
        params: {'stock_symbol': stock_symbol}
      })
      .then(function(response) {
        parent_this.latest_date = response.data['latest_date']
        parent_this.stock_name = response.data['stock_name']
        parent_this.bar_chart_data = response.data['bar_chart_data']
        parent_this.line_chart_data = response.data['line_chart_data']
        parent_this.ai_predict_data = response.data['ai_predict_data']
        var seriesOptions = [],
            seriesCounter = 0,
            names = [parent_this.stock_name];
        parent_this.success_create_line_chart(parent_this.line_chart_data, names, seriesCounter, seriesOptions)
        parent_this.create_bar_chart()
      })
      .catch(function(error) {
        console.log(error);
      });
    },
    success_create_line_chart(data, names, seriesCounter, seriesOptions) {
      var name = names[0]
      var i = 0;
      seriesOptions[0] = {
          name: name,
          data: data
      };
      // As we're loading the data asynchronously, we don't know what order it
      // will arrive. So we keep a counter and create the chart when all the data is loaded.
      seriesCounter += 1;
      if (seriesCounter === names.length) {
          this.create_line_chart(seriesOptions);
      }
    },
    create_line_chart(seriesOptions) {
      parent.this = this
      Highcharts.stockChart('line_chart', {
        rangeSelector: {
            selected: 4
        },
        yAxis: {
            labels: {
                formatter: function () {
                    return (this.value > 0 ? ' + ' : '') + this.value + '%';
                }
            },
            plotLines: [{
                value: 0,
                width: 2,
                color: 'silver'
            }]
        },
        title: {
          text: parent.this.stock_name
        },
        subtitle: {
          text: '預測未來五天價格走勢'
        },
        plotOptions: {
            series: {
                compare: 'percent',
                showInNavigator: true
            }
        },
        tooltip: {
            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
            valueDecimals: 2,
            split: true
        },
        series: seriesOptions
      });
    },
    create_bar_chart() {
      // Build the chart
      const parent_this = this
      Highcharts.chart('bar_chart', {
          chart: {
              plotBackgroundColor: null,
              plotBorderWidth: null,
              plotShadow: false,
              type: 'pie'
          },
          title: {
              text: ''
          },
          subtitle: {
              text: '未來三天的漲幅趨勢機率圖'
          },
          tooltip: {
              pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
          },
          accessibility: {
              point: {
                  valueSuffix: '%'
              }
          },
          plotOptions: {
              pie: {
                  allowPointSelect: true,
                  cursor: 'pointer',
                  dataLabels: {
                      enabled: true,
                      format: '<b>{point.name}</b>: {point.percentage:.0f} %',
                      // connectorColor: 'silver'
                  }
              }
          },
          series: [{
              name: 'Share',
              data: [
                  { name: '漲幅3%以內', y: parent_this.bar_chart_data['three_days_increase_one_percent']},
                  { name: '漲幅3%以上', y: parent_this.bar_chart_data['three_days_increase_three_percent']},
                  { name: '漲跌幅1%以內', y: parent_this.bar_chart_data['three_days_no_change']},
                  { name: '跌幅3%以內', y: parent_this.bar_chart_data['three_days_decrease_one_percent']},
                  { name: '跌幅3%以上', y: parent_this.bar_chart_data['three_days_decrease_three_percent']},
              ]
          }]
      });
    },

  }
}
</script>

<style scoped src="@/assets/ai_predict/css/ai_predict.css">

</style>
