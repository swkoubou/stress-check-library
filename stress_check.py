#simple_MAの改良プログラム
import fitbit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    def some_check(self, data):
        ave=data.value.sum()/len(data)
        maxv=data.value.max()
        minv=min(data.value)
        some={'ave':ave,'max_value':maxv,'min_value':minv}
        return some

    def subtraction(self, day1, day2):
        return day2 - day1