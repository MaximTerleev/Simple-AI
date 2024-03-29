# -*- coding: utf-8 -*-
"""#4 Creating a sound track

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-iax0f7dcF_AdCUgeKoYJAsT3VfjgOS3?usp=sharing

# **Creating a sound track**

"""

from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import IPython.display as ipd
import numpy as np
import librosa

# Load audio
y, sr = librosa.load('/content/wakeup.mp3')
plt.figure(figsize=(15,4))
plt.plot(y)
plt.show()
ipd.Audio(data=y, rate=sr)

# Loop
loops = 3
out = y.copy()
for i in range(loops):
  out = np.concatenate([out, y])
ipd.Audio(data=out, rate=sr)

# Fading
length = 2
for i in range(sr*length, 0, -1):
  out[-i] = out[-i] * i / (sr*length)
ipd.Audio(data=out, rate=sr)

# Speed up
sr_new = sr * 1.5
ipd.Audio(data=out, rate=sr_new)

# Output
write('out.wav', int(sr_new), out)
