#******************************************************
#３年間のランダムな数値データを毎回作成してグラフで表示させるプログラム
#月と年でそれぞれの単純移動平均を求めて破線で表示する
#******************************************************
import numpy as np
randn = np.random.randn
import pandas as pd
import matplotlib.pyplot as plt

#:pd.dare_range - 日付データの作成をするメソッド
#:引 数 - (start='開始時刻', end='終了時刻', freq='指定文字')
#:        ('開始時刻', periods=要素の数)
#:戻り値 - DatetimeIndex 
dtidx = pd.date_range(start='2017-1-1',periods=1095)

#:pd.Series - pandasのデータ構造（１次元配列に似ている）
#:インデックスを０から始まる整数以外にすることができることが特徴。ここでは日時データをインデックスとする。
#:引 数 - (値, index=指定したいデータ) 
#:戻り値 - 配列
ts = pd.Series(randn(1095), index = dtidx)
ts = ts.cumsum()


#データ配列.plot - データをグラフに追加する
ts.plot(style = '<--')

#:pd.rolling_mean - 単純移動平均を求める
#:引数 - (データフレーム（作成した配列）, 平均を求めたい数, nanが出る場合の平均を求める数)
tr=pd.rolling_mean(ts, 30,7)
tr.plot(style='--', c='r')
print(tr[:20])

tb=pd.rolling_mean(ts, 365)
tb.plot(style='--', c='b')

#:グラフの表示
plt.show()
