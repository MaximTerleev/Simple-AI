# -*- coding: utf-8 -*-
"""#19 Create your cartoon

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JGEV6kD8-LeFJhV_95jtC_QRQzw9iCgG?usp=sharing

# **Create your cartoon**

"""

pip install ffmpeg

from IPython.display import HTML
import matplotlib.pyplot as plt
import ffmpeg, base64
from PIL import Image
import numpy as np

# Load scenery image
scenery = np.array(Image.open('/content/scenery.png').convert('RGBA'))
plt.imshow(scenery)

# Load car image
car = np.array(Image.open('/content/car.png').convert('RGBA'))
car[:,:,3][car[:,:,0]==255]=0
plt.imshow(car)

# Create animation
h, w, _ = car.shape
for i in range(0, scenery.shape[1]-car.shape[1], 3):
  frame = scenery.copy()
  frame[260:260+h, i:i+w, :] = frame[260:260+h, i:i+w, :] + car
  frame = Image.fromarray(frame).convert('RGB')
  frame.save('/content/frames/' + str(i).zfill(3) + '.png')

# Assemble frames into video
!cat frames/*.png | ffmpeg -f image2pipe -r 30 -i - -vcodec libx264 -r 30 -pix_fmt yuv420p video.mp4

# Append audio track
!ffmpeg -i video.mp4 -i audio.wav -map 0:v -map 1:a cartoon.mp4

# Play video
video = open('cartoon.mp4', 'rb').read()
url = 'data: video/mp4; base64,' + base64.b64encode(video).decode()
HTML('''<video height="400px" controls><source src="%s"/></video>''' % url)
