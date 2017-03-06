import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#csv形式のデータを読み込む
def input_csv(filename):
    data = pd.read_csv(filename)
    return data

#datetimeindex型のデータを単純移動平均する
def moving_average(data):
    ma=pd.rolling_mean(data, 120)
    return ma

#心拍数の最低値と最高値と平均値を求める
<<<<<<< HEAD
#def check(ma)

=======
def all(data):
    ave=sum(data.value)/len(data.value)
    a=max(data.value)
    b=min(data.value)
    print(ave)
    print(a)
    print(b)
>>>>>>> ace45b85dba8a1fcb64ef503ca73b7d6d662e407
#テスト用
if __name__ == '__main__':
    data=input_csv('heartrate.csv')
    ma=moving_average(data)
<<<<<<< HEAD

    #print(ma.value[120:122])
    print('合計:',sum(ma.value))
   

    '''
    data.plot(style='<--')
    ma.plot(style='--', c='r')
    plt.show()
    '''
    
=======
    all(ma)
    data.plot(style='<--')
    ma.plot(style='--', c='r')
    #plt.show()
>>>>>>> ace45b85dba8a1fcb64ef503ca73b7d6d662e407
