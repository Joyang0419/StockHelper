from crawler.utils import Crawler
import json


class CrawlerStockChip(Crawler):
    data = None

    def __init__(self,  db_url: str = None, url: str = None, headers: dict = None, **params: dict) -> object:
        """
        建構式
        url: 網頁的網址
        headers: 網頁的頭
        **params: 要提供網址的參數
        db_url: 資料庫位置
        """
        # crawler 初始化
        Crawler.__init__(self, url=url, headers=headers, **params)
        self.db_url = db_url  # 資料庫

    def to_database(self):
        pass

    @classmethod
    def main(cls):
        pass


if __name__ == '__main__':
    headers_raw = '''Referer: https://realpython.com/
sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'''

    headers_dict = Crawler.get_headers(headers_raw=headers_raw)

    crawler_stock_chip = CrawlerStockChip(url='https://www.twse.com.tw/fund/T86',
                                          db_url='123',
                                          headers=headers_dict,
                                          response='json',
                                          date='20210309',
                                          selectType='ALL')

    response = crawler_stock_chip.request('get')
    print(response.status_code)
    json_data = json.loads(response.text)
    print(json_data['date'])



