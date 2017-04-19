import fitbit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Stress_Check:
    #コンストラクタ
    def __init__(self):
        self.name=''  

    #datetimeindex型のデータを単純移動平均する
    #１日のデータを計算する
    def day_ave(self, data):
        ma=pd.rolling_mean(data, 120, 1) #データの個数によって変更
        return ma

    #1週間のデータを計算する
    def week_ave(self, data):
        ma=pd.rolling_mean(data, 120, 1)
        return ma

    #1カ月のデータを計算する
    def month_ave(self, data):
        ma=pd.rolling_mean(data, 120, 1)
        return ma

    #心拍数の最低値と最高値と平均値を求める。戻り値は辞書型
    def total_data(self, data):
        ave=data.value.sum()/len(data)
        maxv=data.value.max()
        minv=min(data.value)
        total={'ave':ave,'max_value':maxv,'min_value':minv}
        return total

    def check(self, day1, day2):
        sub = day2 - day1
        if sub >= 5:
            return True
        else:
            return False