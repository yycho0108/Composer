import numpy as np
import pyaudio
from matplotlib import pyplot as plt

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(4),channels=1,rate=44100,output=True)


# FFT
arr = np.arange(44100 * 1) # 44100 = 1 sec, will attain
arr = 2*np.sin(432*(2*np.pi/44100)*arr) # 432 Hz sound
arr = arr.astype(np.float32)

#plt.plot(arr)
#plt.show()

Vjw = np.fft.fft(arr)
freq = np.fft.fftfreq(44100)
plt.plot(freq,Vjw)
plt.show()

stream.write(arr)
stream.stop_stream()
stream.close()

# IFFT
arr2 = np.zeros(44100,dtype=np.complex)
arr2[1 + 432] = 500j #positive
arr2[44100/2 + 1 + 432] = -500j #negative
arr2 = np.fft.ifft(arr2,n=44100,norm="ortho")
arr2 = arr2.astype(np.float32)

#plt.plot(arr2)
#plt.show()

stream.write(arr2)
stream.stop_stream()
stream.close()

p.terminate()
