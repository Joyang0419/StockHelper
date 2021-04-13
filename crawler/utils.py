import requests


class Crawler:
    """
    爬蟲(基底類別)
    """
    # 建構式
    def __init__(self, url: str, method: str, headers: dict, **params):
        """
        建構式
        url: 網頁的網址
        headers: 網頁的頭
        **params: 要提供網址的參數
        """
        self.url = url
        self.headers = headers
        self.method = method
        self.params = params

    # instance method
    def request(self):
        """
        發出request
        """
        response = requests.request(method=self.method,
                                    url=self.url,
                                    headers=self.headers,
                                    params=self.params)
        return response

    # static method
    @staticmethod
    def get_headers(headers_raw):
        """
        處理headers
        """
        headers = {}
        if headers_raw is None:
            return headers
        for row in headers_raw.split("\n"):
            headers[row.split(': ')[0]] = row.split(': ')[1]
        return headers

