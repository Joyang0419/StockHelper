from crawler.utils import Crawler
from datetime import datetime, timedelta
import json
import pymysql
import time
import random


class CrawlerIndustryType(Crawler):
    """
    爬蟲: 股票產業類別
    """
    data = []  # 存放資料區
    db_settings = {
        "host": "192.168.164.94",
        "port": 3306,
        "user": "root",
        "password": "aa329765",
        "db": "stock_helper",
        "charset": "utf8"
    }

    def __init__(self, url: str = None, headers: dict = None, method: str = None, **params):
        """
        建構式
        url: 網頁的網址
        headers: 網頁的頭
        **params: 要提供網址的參數
        """
        # crawler 物件
        Crawler.__init__(self, url=url, headers=headers, method=method, **params)

    def get_data(self, response_text) -> list:
        """抓取資料"""
        json_data = json.loads(response_text)
        print('抓取資料中')
        data = json_data['data']
        print('資料筆數: ', len(data))
        # 產業類別
        industry_type = data['industryType']
        self.data.append(industry_type)

        return self.data

    @staticmethod
    def data_processing(data):
        """資料處理"""
        print('資料處理中')
        # list刪除重複。
        industry_type_list = list(set(data))
        return industry_type_list

    @classmethod
    def to_database(cls, data):
        """資料進入資料庫"""
        print('資料進入資料庫')
        try:
            # 建立Connection物件
            connection = pymysql.connect(**cls.db_settings)
            print('資料庫已建立連結')
            # 建立Cursor物件
            with connection.cursor() as cursor:
                # 資料表相關操作
                # 新增資料SQL語法
                command = "INSERT INTO industry_type (industry_type) VALUES(%s)"
                for i in data:
                    cursor.execute(command, i)

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
        response = self.request()
        # 判斷網頁狀態，200(正常才繼續運作)
        if response.status_code == 200:
            # 抓取資料
            self.get_data(response_text=response.text)
        else:
            print("沒資料: ", self.params['date'])
        return self.data


if __name__ == '__main__':
    headers_raw = '''Referer: https: // realpython.com /
sec-ch-ua: "Google Chrome"; v="89", "Chromium"; v="89", ";Not A Brand"; v="99"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'''

    headers_dict = Crawler.get_headers(headers_raw=headers_raw)

    stock_symbol_list = [2317, 2330, 2329, 2338, 1708]

    for each_stock_symbol in stock_symbol_list:
        url = 'https://marketinfo.api.cnyes.com/mi/api/v1/TWS:' + str(each_stock_symbol) + ':STOCK/info'
        crawler_industry_type = CrawlerIndustryType(url=url,
                                                    headers=headers_dict,
                                                    method='get')
        # 只爬取資料。
        crawler_data = crawler_industry_type.main()
    # 資料清理: 將list中重複資料刪除
    handled_crawler_data = crawler_industry_type.data_processing(data=crawler_data)
    # 資料進入資料庫
    crawler_industry_type.to_database(handled_crawler_data)
