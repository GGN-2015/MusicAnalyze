# 试验场，没什么规矩
from WavObject import WavObject

if __name__ == "__main__":
    wavObject = WavObject("./WAV/Test006.wav")
    spectrum  = wavObject.getSpectrum()

    spectrum.show()
