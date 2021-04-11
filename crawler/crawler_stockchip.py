from crawler.utils import Crawler
from datetime import datetime, timedelta
import json
import pymysql


class CrawlerStockChip(Crawler):
    db_settings = {
        "host": "192.168.164.94",
        "port": 3306,
        "user": "root",
        "password": "aa329765",
        "db": "test",
        "charset": "utf8"
    }

    def __init__(self, url: str = None, method: str = None, headers: dict = None, **params):
        """
        建構式
        url: 網頁的網址
        headers: 網頁的頭
        **params: 要提供網址的參數
        """
        # crawler 物件
        Crawler.__init__(self, url=url, headers=headers, method=method, **params)
        # 存放資料區
        self.data = []

    def get_data(self, response_text) -> list:
        """抓取資料"""
        json_data = json.loads(response_text)
        print('抓取資料日期: ', self.params['date'])
        data = json_data['data']
        print('資料筆數: ', len(data))
        for each_data in data:
            individual_stock = {}  # 個股的資料存放區
            stock_symbol = each_data[0]  # stock symbol: 股票代號
            trading_volume = each_data[18]  # trading volume: 交易量
            individual_stock['stock_symbol'] = stock_symbol
            individual_stock['trading_volume'] = trading_volume
            self.data.append(individual_stock)
            return self.data

    def data_processing(self):
        """資料處理"""
        print('資料處理中')
        for each_data in self.data:
            # 交易量去除千分位，並轉換成數字。
            each_data['trading_volume'] = int(each_data['trading_volume'].replace(',', ''))

    def to_database(self):
        """資料進入資料庫"""
        print('資料進入資料庫')
        try:
            # 建立Connection物件
            connection = pymysql.connect(**self.db_settings)
            # 建立Cursor物件
            with connection.cursor() as cursor:
                # 資料表相關操作
                # 新增資料SQL語法
                command = "INSERT INTO test (stock_symbol, trading_volume, date) VALUES(%s, %s, %s)"
                for each_data in self.data:
                    cursor.execute(command, (each_data['stock_symbol'],
                                             each_data['trading_volume'],
                                             self.params['date']))
                # 儲存變更
                connection.commit()
                cursor.close()
                connection.close()
                print('========================')
        # SQL錯誤時，跳出錯誤原因。
        except Exception as ex:
            print(ex)

    def main(self):
        """
        主程式:
        - request，狀態200，繼續執行。
        - get_data
        - data_processing
        """
        response = Crawler.request(self)
        # 判斷網頁狀態，200(正常才繼續運作)
        if response.status_code == 200:
            # 抓取資料
            self.get_data(response_text=response.text)
            # 資料處理
            self.data_processing()
            # 進入資料庫
            # self.to_database()

        else:
            print("沒資料: ", self.params['date'])
        return self.data

    @staticmethod
    def create_date(start_date: int, end_date: int) -> list:
        """
        時間產生器: 輸入開始日期及結束日期，產生從開始日期到結束日期的所有日期，並存到串列。
        """
        date_list = []
        start_date = datetime.strptime(str(start_date), "%Y%m%d")
        end_date = datetime.strptime(str(end_date), "%Y%m%d")
        delta = timedelta(days=1)
        while start_date <= end_date:
            date_list.append(start_date.strftime("%Y%m%d"))
            start_date += delta
        return date_list


if __name__ == '__main__':
    headers_raw = '''Referer: https://realpython.com/
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'''

    headers_dict = Crawler.get_headers(headers_raw=headers_raw)
    date_list = CrawlerStockChip.create_date(start_date=20200407,
                                             end_date=20200409)
# 使用多線程，用日期每天去爬。
    for each_date in date_list:
        crawler_stock_chip = CrawlerStockChip(url='https://www.twse.com.tw/fund/T86',
                                              headers=headers_dict,
                                              method='get',
                                              response='json',
                                              date=each_date,
                                              selectType='ALL')
        crawler_stock_chip.main()




