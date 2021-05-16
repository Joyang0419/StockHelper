<template>
  <div>
    <div class="input-group" style="padding-top: 10px; padding-bottom: 20px">
      <input type="search" class="form-control rounded" placeholder="請輸入股票代號" aria-label="Search"
      aria-describedby="search-addon" />
      <button type="button" class="btn btn-outline-primary">search</button>
    </div>
    <h6>最近交易日: 2021-04-23</h6>
    <section class="dashboard-counts">
      <div class="container-fluid">
        <div class="row">
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-user"></i></div>
              <div class="name"><strong class="text-uppercase">漲跌幅(%)</strong>
                <div class="count-number">25</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-padnote"></i></div>
              <div class="name"><strong class="text-uppercase">開盤價</strong>
                <div class="count-number">400</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-check"></i></div>
              <div class="name"><strong class="text-uppercase">收盤價</strong>
                <div class="count-number">342</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-bill"></i></div>
              <div class="name"><strong class="text-uppercase">最高價</strong>
                <div class="count-number">123</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-list"></i></div>
              <div class="name"><strong class="text-uppercase">最低價</strong>
                <div class="count-number">92</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-list-1"></i></div>
              <div class="name"><strong class="text-uppercase">成交量(張)</strong>
                <div class="count-number">70</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- K線圖 -->
    <div id="stockData" style="height: 400px; min-width: 310px"></div>
    <!-- 三大法人動向 -->
    <figure class="highcharts-figure">
    <div id="container"></div>
</figure>
  </div>
</template>

<script>
export default {
  name: "StockData",
  data: function() {
    return {
      page_info: {
        latest_info: '',
        stock_data_list: [],
        institution_data_list: []
      }
    }
  },
  created: function() {
    this.get_page_info()
  },
  methods: {
    get_page_info: function () {
      parent.this = this
      axios({
      method: 'get',
      url: 'http://www.stockhelper.com.tw:8889/api/stock_data',
      })
      .then(function (response) {
        console.log(response.data)
        parent.this.draw_stock_data_chart(response.data)
        parent.this.draw_institution_bar_chart()
        response.data
      })
      .catch(function (error) {
        console.log(error);
      });
    },
    draw_stock_data_chart: function (data) {
      // split the data set into ohlc and volume
      var ohlc = [],
          volume = [],
          dataLength = data.length,
          // set the allowed units for data grouping
          groupingUnits = [[
            'week',                         // unit name
            [1]                             // allowed multiples
          ],
          [
            'month',
            [1, 2, 3, 4, 6]
          ]],

          i = 0;

      for (i; i < dataLength; i += 1) {
          ohlc.push([
              data[i][0], // the date
              data[i][1], // open
              data[i][2], // high
              data[i][3], // low
              data[i][4] // close
          ]);

          volume.push([
              data[i][0], // the date
              data[i][5] // the volume
          ]);
      }

      // create the chart
      const stock_data_chart = Highcharts.stockChart('stockData', {

          rangeSelector: {
              selected: 1
          },

          title: {
              text: 'AAPL Historical'
          },

          yAxis: [{
              labels: {
                  align: 'right',
                  x: -3
              },
              title: {
                  text: 'OHLC'
              },
              height: '60%',
              lineWidth: 2,
              resize: {
                  enabled: true
              }
          }, {
              labels: {
                  align: 'right',
                  x: -3
              },
              title: {
                  text: 'Volume'
              },
              top: '65%',
              height: '35%',
              offset: 0,
              lineWidth: 2
          }],

          tooltip: {
              split: true
          },

          series: [{
              type: 'candlestick',
              name: 'AAPL',
              data: ohlc,
              dataGrouping: {
                  units: groupingUnits
              }
          }, {
              type: 'column',
              name: 'Volume',
              data: volume,
              yAxis: 1,
              dataGrouping: {
                  units: groupingUnits
              }
          }]
      });
    },
    draw_institution_bar_chart() {
      Highcharts.chart('container', {
        title: {
            text: '三大法人動向'
        },
        subtitle: {
            text: '單位(張)'
        },
        xAxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        },
        series: [{
            type: 'column',
            colorByPoint: true,
            data: [29.9, 71.5, -1000, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
            showInLegend: false
        }],
      });
    }
  }
}
</script>

<style scoped src="@/assets/stock_data/css/stock_data.css">

</style>
