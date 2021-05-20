import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import pathlib


def three_days_predict(dataframe=None):
    # yyyy/mm/dd -> year, month, day
    aaa = pd.read_csv("qqq.csv")

    return '123'
    # return dataframe
    dataframe = dataframe.rename(columns={'date': 'Date', 'opening_price': 'Open', 'closing_price': 'Close',
                                          'highest_price': 'High', 'lowest_price': 'Low', 'volume': 'Volume'}
                                 , inplace=False)
    # dataframe["Date"] = dataframe["date"]
    dataframe["Date"] = pd.to_datetime(dataframe["Date"])
    dataframe["year"] = dataframe["Date"].dt.year
    dataframe["month"] = dataframe["Date"].dt.month
    dataframe["date"] = dataframe["Date"].dt.day
    dataframe["day"] = dataframe["Date"].dt.dayofweek + 1
    # 轉完後，drop column: date，無法進模型
    # 去除不必要的資料後 -> Open. High, Low, Close, Volume year  month  date  day
    dataframe = dataframe.drop(columns=['Date'])
    # dataframe = dataframe.drop(columns=['Date', 'id', 'stock_basic_info_id'])
    # dataframe.to_csv('123.csv')
    # return '123'

    # return dataframe.columns
    #  用pandas轉成numpy數組
    x = dataframe.values
    # 數據歸一化(最大最小方法)
    min_max_scaler = MinMaxScaler()
    min_max_scaler.fit(x)
    x = min_max_scaler.transform(x)
    # 讀取模型
    model_path = pathlib.Path('/var/www/html/app/views/ai/models/three_days_price_predict/DNN_Model_5Probability.h5')  # 模型路徑
    load_model = tf.keras.models.load_model(model_path)  # 載入模型
    # 使用模型預測
    model_output = load_model.predict(x)
    # data: [漲跌幅小於一趴, 漲幅大於一趴小於三趴, 跌幅大於一趴小於三趴, 漲幅大於三趴, 跌幅大於三趴]
    return model_output[-1]  # 回傳model_output最後一筆


if __name__ == '__main__':
    # 讀取資料
    # dataframe = pd.read_excel("2317_data.xlsx")
    dataframe = pd.read_csv("qqq.csv")
    print(dataframe)
    # dataframe.to_csv('qqq.csv')
    # print(df)
    # three_days_predict_output = three_days_predict()
    # print(three_days_predict_output)

