<template>
  <div>
    <breadcrumb></breadcrumb>
    <div class="input-group" style="padding-top: 10px; padding-bottom: 20px">
      <input type="search" class="form-control rounded" placeholder="請輸入股票代號" aria-label="Search"
      aria-describedby="search-addon"/>
      <button type="button" class="btn btn-outline-primary" @click="stock_symbol_search()">search</button>
    </div>
    <h6>最近交易日: 2021-04-23</h6>
    <!-- line chart -->
    <div id="line_chart" style="height: 400px; min-width: 310px;"></div>
      <div class="row">
        <figure class="highcharts-figure">
          <!-- bar chart -->
          <div class="col-md-12" id="bar_chart"></div>
        </figure>
        <div class="col-md-5">
          <div class="panel panel-scrolling">
            <div class="panel-heading">
              <h1 class="panel-title" style="text-align:center">AI智能預測</h1>
            </div>
            <div class="panel-body">
              <ul>
                <li>未來5天的價格: 22.4, 22.6, 22.3, 22.5, 22.6。</li>
                <li>明日價格預測
                  <ul>
                    <li>無動靜: 41%</li>
                    <li>漲幅3%以內: 1%</li>
                    <li>漲幅3%以上: 1%</li>
                    <li>跌幅3%以內: 47%</li>
                    <li>跌幅3%以上: 10%</li>
                  </ul>
                </li>
                <div class="col-md-3 button"><a href="#" class="btn btn-success" data-toggle="modal" data-target="#CreateTrade">執行交易</a></div>
              </ul>
            </div>
          </div>
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
      user_email: '',
    }
  },
  created() {
    this.get_page_info()
  },
  mounted() {
    this.create_bar_chart()
  },
  methods: {
    get_page_info() {
      this.get_line_chart_data()
    },
    get_line_chart_data() {
      parent.this = this
      axios({
        method: 'get',
        url: 'https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/msft-c.json',
      })
      .then(function(response) {
        var seriesOptions = [],
            seriesCounter = 0,
            names = ['MSFT'];
        parent.this.success(response.data, names, seriesCounter, seriesOptions)
      })
      .catch(function(error) {
        console.log(error);
      });

    },
    create_line_chart(seriesOptions) {
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
          text: '第一金'
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
    success(data, names, seriesCounter, seriesOptions) {
      var name = 'MSFT'
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
    create_bar_chart() {
      // Build the chart
      Highcharts.chart('bar_chart', {
          chart: {
              plotBackgroundColor: null,
              plotBorderWidth: null,
              plotShadow: false,
              type: 'pie'
          },
          title: {
              text: 'Browser market shares in January, 2018'
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
                      format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                      // connectorColor: 'silver'
                  }
              }
          },
          series: [{
              name: 'Share',
              data: [
                  { name: 'Chrome', y: 61.41 },
                  { name: 'Internet Explorer', y: 11.84 },
                  { name: 'Firefox', y: 10.85 },
                  { name: 'Edge', y: 4.67 },
                  { name: 'Safari', y: 4.18 },
                  { name: 'Other', y: 7.05 }
              ]
          }]
      });
    },

  }
}
</script>

<style scoped src="@/assets/ai_predict/css/ai_predict.css">

</style>
