import csv
import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# 引  数 ： numpy配列の心拍数データ
# 返り値 ： ストレス指標値
def calc(hr):
	VLF_MIN = 0.0033 #[Hz] 補正値
	VLF_MAX = 0.04   #[Hz] 
	LF_MIN = 0.04    #[Hz]
	LF_MAX = 0.15    #[Hz]
	HF_MIN = 0.15    #[Hz]
	HF_MAX = 0.4     #[Hz]
	
	lf_pow = 0   # LF帯のパワースペクトル
	hf_pow = 0   # HF帯のパワースペクトル
	vlf_pow = 0  # VLF帯のパワースペクトル
	tp = 0       # 0~0.4[Hz]のパワースペクトルのトータルパワー
	lf_norm = 0  # LF補正値
	hf_norm = 0  # HF補正値
	lf_hf = 0    # HF/LF比
	lf_hf_norm = 0    # 補正値を使用したHF/LF比

	# 心拍数をRRIに置き換える
	# [回/min] -> [msec]
	N = len(hr)
	rri = [0 for i in range(N)]
	for i in range(N):
		rri[i] = (float(60) / hr[i]) * 1000
		
	# パワースペクトル密度の計算
	hz, p = signal.periodogram(rri, 1)

	# LFとHF
	N = len(hz)
	lf = [0 for i in range(N)]
	hf = [0 for i in range(N)]

	# LF成分とHF成分は各領域のパワースペクトル成分の総和
	# LF成分・HF成分・VLF成分・トータルパワーの算出
	for i in range(N):
		if(hz[i] > VLF_MIN and hz[i] < VLF_MAX):
			vlf_pow += p[i]
		if(hz[i] > LF_MIN and hz[i] < LF_MAX):
			lf_pow += p[i]
		if(hz[i] > HF_MIN and hz[i] < HF_MAX):
			hf_pow += p[i]
		if(hz[i] < HF_MAX):
			tp += p[i]

	# LFとHFの補正値の計算
	# lf_norm = lf_pow / (tp - vlf_pow) * 100
	# hf_norm = hf_pow / (tp - vlf_pow) * 100


	# LF/HF比
	lf_hf = lf_pow / hf_pow
	
	# LF : HF = x : 1
	#lf_hf_norm = lf_norm / hf_norm

	return lf_hf
	

if __name__ == "__main__":

	# csvからpandasデータフレーム形式で心拍数データを取得
	df = pd.read_csv('heartrate_data.csv', index_col='time')

	# pandasデータフレームをnumpyの配列に変換
	# dfのカラムのvalueがnpの配列になる
	hr = np.array(df.values.flatten())

	lh = calc(hr)

	print('- ストレス判断 -')
	if(lh < 2.0):
		print('  基準値  ')
	elif(lh < 5.0):
		print('  注  意  ')
	else:
		print('  要注意  ')
