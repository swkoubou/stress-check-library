import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#csv形式のデータを読み込む
data = pd.read_csv("heartrate.csv")


sma=pd.rolling_mean(data, 120)
data.plot(style='<--')
sma.plot(style='--', c='r')

plt.show()