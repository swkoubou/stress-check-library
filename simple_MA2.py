import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#csv形式のデータを読み込む
def input_csv(filename):
    data = pd.read_csv(filename)
    return data

#datatimeindex型のデータを単純移動平均する
def moving_average(data):
    ma=pd.rolling_mean(data, 120)
    return ma

#心拍数の最低値と最高値と平均値を求める
#def
    #

#テスト用
if __name__ == '__main__':
    data=input_csv('heartrate.csv')
    ma=moving_average(data)

    data.plot(style='<--')
    ma.plot(style='--', c='r')
    plt.show()
