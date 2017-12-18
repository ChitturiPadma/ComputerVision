
# coding: utf-8

# In[7]:

import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt


# In[8]:

img = cv2.imread('/home/padmach/data/pyimagesearch/flower1.jpg')
cv2.imshow('',img)
cv2.waitKey(0)


# In[15]:

kernelSizes =[(3,3),(3,5),(9,9), (15, 15), (5, 3), (9,19), (19,19)]

#Applying average blurring
for (kx, ky) in kernelSizes:
    blurred = cv2.blur(img, (kx,ky))
    cv2.imshow('Average ({}, {})'.format(kx, ky), blurred)
    cv2.waitKey(0)


# In[14]:

#Applying Gaussian blurring

for (kx, ky) in kernelSizes:
    blurred = cv2.GaussianBlur(img, (kx,ky),0) #0 indicates that standard deviation is computed based on kernel size
    cv2.imshow('Gaussian ({},{})'.format(kx,ky), blurred)
    cv2.waitKey(0)


# In[18]:

#Applying Median filtering

for k in (3, 9, 15, 19, 21, 23, 25, 27, 29):
    blurred = cv2.medianBlur(img, k)
    cv2.imshow('Median {}'.format(k), blurred)
    cv2.waitKey(0)


# In[21]:

#Applying Bilateral filtering
params =[(11, 21, 7), (11, 41, 21),(11, 61, 39)]

for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(img, diameter, sigmaColor, sigmaSpace)
    cv2.imshow('Blurred d ={}, sc = {}, ss = {}'.format(diameter, sigmaColor, sigmaSpace), blurred)
    cv2.waitKey(0)


# In[ ]:



