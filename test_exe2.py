#ライブラリ stress_check.pyの動作を確認するプログラム
from stress_check import *

#心拍数を取得するライブラリ
class Get_Heart_Rate:
    #コンストラクタ
    def __init__(self):
        self.name=''

    #日付を指定してその１日の心拍数を取得する(１分)
    def day_time_series(self, date, ID):
        authd_client = fitbit.Fitbit(ID['CLIENT_ID'], ID['CLIENT_SECRET'], access_token=ID['ACCESS_TOKEN'], refresh_token=ID['REFRESH_TOKEN'])
        data_min = authd_client.intraday_time_series('activities/heart', base_date=date, detail_level='1min')
        heart_min = data_min["activities-heart-intraday"]["dataset"]
        heart_df = pd.DataFrame.from_dict(heart_min)
        return heart_df

    #できてない
    def week_time_series(self, date, ID):
        heart_df = day_time_series(date, ID)
        print(heart_df[0])
        for i in range(2):
            date = date + pd.offsets.Day()
            h_df = day_time_series(date, ID)
            print(h_df[0])
            heart_df.append(h_dfd, ignore_index=True)
        return heart_df

    def month_time_series(self, date, ID):
        return 0

if __name__ == '__main__':

    #アクセストークンとリフレッシュトークンは毎回手動で変更
    ID={'CLIENT_ID':'2284BG',
    'CLIENT_SECRET':"b2a1b298d81cf7d4893974c1c9eedb98",
    'ACCESS_TOKEN':'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1RkdQQ1kiLCJhdWQiOiIyMjg0QkciLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyaHIiLCJleHAiOjE0OTAwMTI1MDQsImlhdCI6MTQ4OTk4MzcwNH0.CuIzAv7NcJ_T9wnCT7hPO164jhLJ5QjcpSrPqcaCHME',
    'REFRESH_TOKEN':'08c8403844551220b07be3f26599907f2603be8eb13bd13e6b7a5a16e4a09957'}

    #クラスの宣言
    sc=Stress_Check()
    ghr = Get_Heart_Rate()

    #日付の指定
    date = pd.to_datetime('2017-03-09')
    yesterday = pd.to_datetime('2017-03-08')

    #心拍数データの読み込み
    heart_df = ghr.day_time_series(date, ID)
    heart_df2 = ghr.day_time_series(yesterday, ID)

    #心拍数データの計算
    ma=sc.day_moving_average(heart_df)
    ma2=sc.day_moving_average(heart_df2)

    #心拍数の平均、最大、最小を求める
    some=sc.some_data(ma)
    print('-今日の心拍数-')
    print('平均:',some['ave'])
    print('最大:',some['max_value'])
    print('最小:',some['min_value'])
    some2=sc.some_data(ma2)
    print('-翌日の心拍数-')
    print('平均:',some2['ave'])
    print('最大:',some2['max_value'])
    print('最小:',some2['min_value'])    

    sub=sc.stress_check(some['ave'], some2['ave'])
    print('心拍数の差:', some2['ave']-some['ave'])
    if sub == True:
        print('疲れてませんか？')
    else:
        print('疲れはないようです')


    '''
    #グラフの表示
    ma.plot(style='--')
    ma2.plot(style='--', c='r')
    plt.show()
    '''
