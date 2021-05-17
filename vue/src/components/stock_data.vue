<template>
  <div>
    <div class="input-group" style="padding-top: 10px; padding-bottom: 20px">
      <input type="search" class="form-control rounded" placeholder="請輸入股票代號" aria-label="Search"
      aria-describedby="search-addon" v-model="stock_symbol" />
      <button type="button" class="btn btn-outline-primary" @click="stock_symbol_search()">search</button>
    </div>
    <h6>最近交易日: {{ page_info.latest_info['date'] }}</h6>
    <section class="dashboard-counts">
      <div class="container-fluid">
        <div class="row">
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-user"></i></div>
              <div class="name"><strong class="text-uppercase">漲跌幅(%)</strong>
                <div class="count-number">{{ page_info.latest_info['percent'] }}</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-padnote"></i></div>
              <div class="name"><strong class="text-uppercase">開盤價</strong>
                <div class="count-number">{{ page_info.latest_info['opening_price'] }}</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-check"></i></div>
              <div class="name"><strong class="text-uppercase">收盤價</strong>
                <div class="count-number">{{ page_info.latest_info['closing_price'] }}</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-bill"></i></div>
              <div class="name"><strong class="text-uppercase">最高價</strong>
                <div class="count-number">{{ page_info.latest_info['highest_price'] }}</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-list"></i></div>
              <div class="name"><strong class="text-uppercase">最低價</strong>
                <div class="count-number">{{ page_info.latest_info['lowest_price'] }}</div>
              </div>
            </div>
          </div>
          <!-- Count item widget-->
          <div class="col-xl-2 col-md-4 col-6">
            <div class="wrapper count-title d-flex">
              <div class="icon"><i class="icon-list-1"></i></div>
              <div class="name"><strong class="text-uppercase">成交量(張)</strong>
                <div class="count-number">{{ page_info.latest_info['volume'] }}</div>
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
      stock_symbol: '',
      page_info: {
        latest_info: '',
      }
    }
  },
  created: function() {
    this.get_page_info('0050')
  },
  methods: {
    stock_symbol_search() {
      this.get_page_info(this.stock_symbol)
      this.stock_symbol = ''
    },
    get_page_info: function(stock_symbol) {
      parent.this = this
      axios({
      method: 'get',
      url: 'http://www.stockhelper.com.tw:8889/api/stock_data',
      params: {'stock_symbol': stock_symbol}
      })
      .then(function (response) {
        console.log(response)
        parent.this.page_info.latest_info = response.data['latest_info']
        parent.this.draw_stock_data_chart(response.data['stock_data'])
        parent.this.draw_institution_bar_chart(response.data['stock_chip_data'])
        response.data
      })
      .catch(function (error) {
        console.log(error);
      });
    },
    draw_stock_data_chart: function (data) {
      // split the data set into ohlc and volume
      // console.log(data['data_list'])
      var ohlc = [],
          volume = [],
          dataLength = data['data_list'].length,
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
              data['data_list'][i][0], // the date
              data['data_list'][i][1], // open
              data['data_list'][i][2], // high
              data['data_list'][i][3], // low
              data['data_list'][i][4] // close
          ]);

          volume.push([
              data['data_list'][i][0], // the date
              data['data_list'][i][5] // the volume
          ]);
      }

      // create the chart
      const stock_data_chart = Highcharts.stockChart('stockData', {
          plotOptions: {
            candlestick: {
              color: 'palegreen',
              upColor: 'lightcoral'
            }
          },
          rangeSelector: {
              selected: 1
          },

          title: {
              text: data['stock_name']
          },

          yAxis: [{
              labels: {
                  format: '{value:.1f}',
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
              name: data['stock_name'],
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
    draw_institution_bar_chart(data) {
      Highcharts.chart('container', {
        title: {
            text: '三大法人動向'
        },
        subtitle: {
            text: '單位(張)'
        },
        xAxis: {
            categories: data['date_list'],
        },
        series: [{
            type: 'column',
            name: '三大法人買超',
            colorByPoint: false,
            data: data['data_list'],
            showInLegend: false
        }],
      });
    }
  }
}
</script>

<style scoped src="@/assets/stock_data/css/stock_data.css">

</style>
