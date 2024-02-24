# This code works on mono channel wav file only

import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("Youssef.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

timeInSec = n_samples/sample_freq

signal_array = np.frombuffer(signal_wave, dtype=np.int16)  # Convert  bytes object to numpy array

# To create a figure, you need x and y samples
times = np.linspace(0, timeInSec, num=n_samples)

# print(times)
# print(signal_array)

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.xlabel("Time(s)")
plt.ylabel("Sample Wave")
plt.xlim(0, timeInSec)
plt.show()