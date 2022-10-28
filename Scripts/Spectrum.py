# 频谱类
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

from math import floor

# 频谱类
class Spectrum:

    # 使用 ndarray 构造频谱，需要一个频谱和一个总秒数
    def __init__(self, spectrum: np.ndarray, timeSecond: float) -> None:
        assert type(spectrum)   == np.ndarray
        assert type(timeSecond) == float
        self.data               =  spectrum
        self.timeSecond         =  timeSecond

    # 获取数据部分
    def getData(self):
        return self.data.copy()

    # 获取总时长
    def getTotalTime(self):
        return self.timeSecond

    # 获取某一时刻的频谱
    def getDataByTime(self, timeSecond: float):
        assert type(timeSecond) == float
        assert 0 <= timeSecond and timeSecond <= self.getTotalTime()

        singleLen = self.getTotalTime() / len(self.data) # data 横坐标 1 对应多少秒
        pos       = floor(timeSecond / singleLen)

        assert 0 <= pos and pos <= len(self.data)
        return (self.data[pos,:]).copy()

    # 使用 matplotlib 显示频谱
    def show(self) -> None:
        plt.figure(figsize=(19, 12))
        librosa.display.specshow(self.data, y_axis='linear')
        plt.colorbar(format = '%+2.0f dB')
        plt.title('Linear-frequency power spectrogram of aloe')
        plt.show()
