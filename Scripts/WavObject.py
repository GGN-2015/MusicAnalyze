# 频谱图生成器
import librosa
import numpy as np

from Spectrum import Spectrum

# WavObject : 描述一个 WAV 文件
class WavObject:

    # 根据一个 WAV 文件初始化
    def __init__(self, wavFilePath) -> None:
        data, samplingRate = librosa.load(wavFilePath)
        self.data          = data
        self.samplingRate  = samplingRate

    # 获取 WAV 的数据部分的备份，保证原始对象不会被修改
    def getData(self):
        return self.data.copy()

    # 获取 WAV 的采样率，由于采样率是整数，所以不需要拷贝
    def getSamplingRate(self):
        return self.samplingRate

    # 获取音乐的总时长
    def getTotalTime(self):
        return len(self.data) / self.samplingRate

    # 获取频谱
    def getSpectrum(self):
        D = librosa.amplitude_to_db(np.abs(librosa.stft(self.data)), ref=np.max)
        return Spectrum(D, self.getTotalTime())
