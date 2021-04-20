from utils import Crawler
import json


class CrawlerBasicInfo(Crawler):
    """
    爬蟲: 股票基本資訊
    - stock_basic_info:
        - stock_symbol
        - stock_name
        - industry_type_id
    - stock_basic_info_detail:
        - stock_symbol_id
        - company_address
        - company_phone_number
        - business_description
        - establishment_day
        - TWSE_listed_day
        - OTC_listed_day
    - industry_type
        - id
        - name
    """
    db_settings = {
        "host": "172.18.0.101",
        "port": 3306,
        "user": "root",
        "password": "stockhelper",
        "db": "stockhelper",
        "charset": "utf8"
    }
    # 存放產業類別
    industry_type_list = []

    def __init__(self, url: str = None, method: str = None, headers: dict = None, **params):
        """
        建構式
        url: 網頁的網址
        headers: 網頁的頭
        **params: 要提供網址的參數
        """
        # crawler 物件
        Crawler.__init__(self, url=url, headers=headers, method=method, **params)
        # 資料存放區
        self.data = []
        # 判斷是否要新增industry_type，預設False
        self.industry_type_status = False

    def get_data(self, response_text) -> list:
        """抓取資料"""
        json_data = json.loads(response_text)
        print('抓取資料中')
        data = json_data['data']
        print('資料筆數: ', len(data))
        self.data = data
        return self.data

    def data_processing(self):
        """
        資料處理
        - 判別產業類別是否要新增資料
        """
        # 判斷產業類別是否已存在，若不存在加入industry_type。
        if self.data['industryType'] not in self.industry_type_list:
            self.industry_type_status = True
            self.industry_type_list.append(self.data['industryType'])
            print("已加入產業類別存放串列:{}".format(self.data['industryType']))

    def to_database(self):
        """
        資料進入資料庫
        - industry_type
        - stock_basic_info
        - stock_basic_info_detail
        """


if __name__ == '__main__':
    headers_raw = '''authority: marketinfo.api.cnyes.com
method: GET
path: /mi/api/v1/TWS:1503:STOCK/info
scheme: https
accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
origin: https://invest.cnyes.com
referer: https://invest.cnyes.com/
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36
x-cnyes-app: unknown
x-platform: WEB, WEB
x-system-kind: FUND_OLD_DRIVER'''
    # 處理headers
    headers_dict = Crawler.get_dict(str_raw=headers_raw)
    # 創造crawler_basic_info物件
    crawler_basic_info = CrawlerBasicInfo(url='https://marketinfo.api.cnyes.com/mi/api/v1/TWS:1503:STOCK/info',
                                          headers=headers_dict,
                                          method='get')
    response = crawler_basic_info.request()
    # 拿取資料
    crawler_basic_info.get_data(response_text=response.text)
    # 資料處理: 判斷是否要加入新產業類別
    crawler_basic_info.data_processing()




