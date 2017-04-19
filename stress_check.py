import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class StressCheck:
    #コンストラクタ
    def __init__(self,data):
        self.data = data

    #datetimeindex型のデータを単純移動平均する
    #１日のデータを計算する
    def day_ave(self):
        ma = pd.rolling_mean(self.data, 120, 1) #データの個数によって変更
        return ma　
    #1週間のデータを計算する
    def week_ave(self):
        ma = pd.rolling_mean(self.data, 120, 1)
        return ma

    #1カ月のデータを計算する
    def month_ave(self):
        ma = pd.rolling_mean(self.data, 120, 1)
        return ma

    #心拍数（平均値）
    def ave_data(self, data):
        ave = data.value.sum()/len(data)
        return ave

    #心拍数（最大値）
    def max_data(self,data):
        maxv = data.value.max()
        return maxv
    #心拍数（最小値）
    def min_data(self,data):
        minv = min(data.value)
        return minv
    #2つのデータを比較してストレスがあるかどうかを判断する
    def check(self, day1, day2):
        sub = day2 - day1
        if sub >= 5:
            return True
        else:
            return False
