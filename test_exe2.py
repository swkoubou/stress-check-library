#ライブラリ stress_check.pyの動作を確認するプログラム
from stress_check import *

if __name__ == '__main__':
    sc=Stress_Check()
    ghr = Get_Heart_Rate()

    DATE = pd.to_datetime("2017-03-08")
    nextDATE = DATE + pd.offsets.Day()

    heart_df = ghr.day_time_series(DATE)
    heart_df2 = ghr.day_time_series(nextDATE)

    ma=sc.day_moving_average(heart_df)
    ma2=sc.day_moving_average(heart_df2)

    some=sc.some_check(ma)
    print('-１日目の心拍数-')
    print('平均:',some['ave'])
    print('最大:',some['max_value'])
    print('最小:',some['min_value'])
    some2=sc.some_check(ma2)
    print('-2日目の心拍数-')
    print('平均:',some2['ave'])
    print('最大:',some2['max_value'])
    print('最小:',some2['min_value'])
    some3=some['ave']-some2['ave']
    print('前日との差',some3)
    ma.plot(style='--')
    ma2.plot(style='--', c='r')
    plt.show()
    #青いグラフが１日目のデータ
    #赤いグラフが２日目のデータ
