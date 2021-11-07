# -*- coding: utf-8 -*-
"""#6 Convert speech into text

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13tQWY3ofn_Ur_ZGKpnrfBhcp-yxnIrgk?usp=sharing

# **Convert speech into text**

"""

pip install SpeechRecognition

from scipy.io.wavfile import write
import speech_recognition as sr
import IPython.display as ipd
import numpy as np
import librosa

# Read audio file
audio, srate = librosa.load('/content/Phrase.m4a')
ipd.Audio(data=audio, rate=srate)

# Convert to 32-bit integers
int_audio = np.round(audio*2**32).astype('int32')
print(2**32)

# Write to PCM WAV
write('output.wav', srate, int_audio)
ipd.Audio(data=int_audio, rate=srate)

with sr.AudioFile('/content/output.wav') as source:
  r = sr.Recognizer()
  speech = r.record(source)
text = r.recognize_google(speech, language='en')
print(text)
