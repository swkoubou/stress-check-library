#simple_MAの改良プログラム
import fitbit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ID
CLIENT_ID =  "2284BG"
CLIENT_SECRET  = "b2a1b298d81cf7d4893974c1c9eedb98"
ACCESS_TOKEN =  "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1RkdQQ1kiLCJhdWQiOiIyMjg0QkciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyaHIiLCJleHAiOjE0ODkxNTY3MTEsImlhdCI6MTQ4OTEyNzkxMX0.-Wi1bj-IC18zLgqakSuzZDqTqm98iEw_lS4KHRCoG3Y"
REFRESH_TOKEN =  "4736c50702b9e8f0331a9ea58f1cbdf4fd896e5543d8f94588a688f11fc6b344"


class Stress_Check:
    #コンストラクタ
    def __init__(self):
        self.name=''

    #csv形式のデータを読み込む 戻り値ははDataFrame
    def input_csv(self, filename):
        data = pd.read_csv(filename)
        return data

    #datetimeindex型のデータを単純移動平均する
    #１日のデータを計算する
    def day_moving_average(self, data):
        ma=pd.rolling_mean(data, 120, 1) #データの個数によって変更
        return ma

    #1週間のデータを計算する
    def week_moving_average(self, data):
        ma=pd.rolling_mean(data, 120, 1)
        return ma

    #1カ月のデータを計算する
    def month_moving_average(self, data):
        ma=pd.rolling_mean(data, 120, 1)
        return ma

    #心拍数の最低値と最高値と平均値を求める。戻り値は辞書型
    def some_check(self,data):
        ave=data.value.sum()/len(data)
        maxv=data.value.max()
        minv=min(data.value)
        some={'ave':ave,'max_value':maxv,'min_value':minv}
        return some


class Get_Heart_Rate:
    #コンストラクタ
    def __init__(self):
        self.name=''

    #日付を指定してその１日の心拍数を取得する(１分)
    def day_time_series(self, date):
        authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
        data_min = authd_client.intraday_time_series('activities/heart', date, detail_level='1min')
        heart_min = data_min["activities-heart-intraday"]["dataset"]
        heart_df = pd.DataFrame.from_dict(heart_min)
        return heart_df

    def week_time_series(self, date):
        return 0

    def month_time_series(self, date):
        return 0