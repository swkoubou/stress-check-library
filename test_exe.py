#ライブラリ simple_MA.pyの動作を確認するプログラム
from simple_MA import *

if __name__ == '__main__':
    sc=Stress_Check()
    print('go')
    data=sc.input_csv('heartrate.csv')
    ma=sc.day_moving_average(data)

    some=sc.some_check(ma)
    print('平均:',some['ave'])
    print('最大:',some['max_value'])
    print('最小:',some['min_value'])
    
    data.plot(style='--')
    ma.plot(style='--', c='r')
    plt.show()
    #青いグラフが元データ
    #赤いグラフが変換したデータ