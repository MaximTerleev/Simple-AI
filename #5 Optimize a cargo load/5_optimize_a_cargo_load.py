# -*- coding: utf-8 -*-
"""#5 Optimize a cargo load

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14q8DNtzgLDsa5JY_qeEYxOLDXnyenFUV?usp=sharing

# **Optimize a cargo load**

"""

import matplotlib.pyplot as plt
import numpy as np
import random

# Create container and cargos
container = [10,15]
boxes = [[2,3],[3,2],[3,1],[1,3],[3,3]]

# Generate location maps
locations=[]
empty_container = np.zeros(shape=(container[0],container[1]))
for box in boxes:
 for i in range(container[0]-box[0]+1):
   for j in range(container[1]-box[1]+1):
     location = empty_container.copy()
     location[i:i+box[0],j:j+box[1]] = np.ones((box[0],box[1]))
     locations.append(location)
locations = np.concatenate([[empty_container],locations])
locations.shape

# Evolution parameters
nbots  = 1000
nsurv  = 500
bLen   = 50
mut    = 0.5
epochs = 1000

# Initial population
popul = np.zeros((nbots,bLen))
for i in range(nbots):
  n_boxes = random.randint(0,bLen)
  popul[i,:n_boxes] = np.random.choice(range(locations.shape[0]), n_boxes, replace=False)
popul = np.array(popul).astype('int')

# Evolution

for epoch in range(epochs):

  # natural selection
  val = []
  for i in range(nbots):
    load = empty_container.copy()
    for j in range(bLen): load = load+locations[popul[i,j]]
    value = load.sum()
    if np.sum(load>1)>0: value=0
    val.append([value, i])
  
  val = sorted(val, reverse=True)[:nsurv]
  survpopul = [popul[v[1]] for v in val]
  popul = survpopul
     
  # generate new population from best bots
  for i in range(nbots-nsurv):
    newbot = random.choice(survpopul).copy()
    if np.where(newbot==0)[0].shape[0] > 0:
      pos = np.where(newbot==0)[0][0]
    else: pos = 49
    newbot[pos] = random.randint(0,locations.shape[0]-1)
    if random.random() < mut:
      newbot[random.randint(0,49)] = 0
    popul.append(newbot)
  
  popul = np.array(popul)

  if epoch % 100 == 0 or epoch == epochs:
    print('Epoch:', epoch, ' Value:', val[0][0])

# Show the resulting load
load = empty_container
for j in range(bLen):
  load = load + locations[popul[0,j]] * (4*j+50)
plt.imshow(load)
plt.show()
