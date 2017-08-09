from scipy import signal

# 引  数 ： numpy配列の心拍数データ
# 返り値 ： ストレス指標値
def calc(hr):
	LF_MIN = 0.04    #[Hz]
	LF_MAX = 0.15    #[Hz]
	HF_MIN = 0.15    #[Hz]
	HF_MAX = 0.4     #[Hz]
	
	lf_pow = 0   # LF帯のパワースペクトル
	hf_pow = 0   # HF帯のパワースペクトル
	lf_hf = 0    # HF/LF比

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
		if(hz[i] > LF_MIN and hz[i] < LF_MAX):
			lf_pow += p[i]
		if(hz[i] > HF_MIN and hz[i] < HF_MAX):
			hf_pow += p[i]

	# LF/HF比
	lf_hf = lf_pow / hf_pow

	return lf_hf
