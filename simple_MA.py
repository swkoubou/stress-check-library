import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#csv形式のデータを読み込む
def input_csv(filename):
    data = pd.read_csv(filename)
    return data

#datatimeindex型のデータ
def moving_average(data):
    sma=pd.rolling_mean(data, 120)
    data.plot(style='<--')
    sma.plot(style='--', c='r')

#テスト用
if __name__ == '__main__':
    data=input_csv('heartrate.csv')
    moving_average(data)
    plt.show()
