<template>
  <div>
    <breadcrumb></breadcrumb>
    <div class="input-group" style="padding-top: 10px; padding-bottom: 20px">
      <input type="search" class="form-control rounded" placeholder="請輸入股票代號" aria-label="Search"
      aria-describedby="search-addon" v-model="stock_symbol" />
      <button type="button" class="btn btn-outline-primary" @click="stock_symbol_search()">search</button>
    </div>
    <h6>最近交易日: 2021-04-23</h6>
    <div id="qqq" style="height: 400px; min-width: 310px"></div>
  </div>
</template>

<script>
import Breadcrumb from './breadcrumb'
export default {
  name: "ai_predict",
  components: {
    Breadcrumb
  },
  data() {
    return {
      a: 456,
    }
  },
  created() {
    this.get_line_chart_data()
  },
  mounted() {
  },
  methods: {
    get_page_info() {
      this.get_line_chart_data()
      // console.log(1)

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
    create_chart(seriesOptions) {
      Highcharts.stockChart('qqq', {
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
      var i = names.indexOf(name);
      seriesOptions[i] = {
          name: name,
          data: data
      };
      // As we're loading the data asynchronously, we don't know what order it
      // will arrive. So we keep a counter and create the chart when all the data is loaded.
      seriesCounter += 1;
      if (seriesCounter === names.length) {
          this.create_chart(seriesOptions);
      }
    }

  }
}
</script>

<style scoped>

</style>
