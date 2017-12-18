
# coding: utf-8

# In[1]:

import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt


# In[11]:

img = cv2.imread('/home/padmach/data/pyimagesearch/flower3.jpg')
cv2.imshow('',img)
cv2.waitKey(0)


# In[4]:

(B,G,R) = cv2.split(img)


# In[3]:

for (name, channel) in zip(('B', 'G', 'R'), cv2.split(img)):
    cv2.imshow(name, channel)
    cv2.waitKey(0)


# In[9]:

cv2.imshow('',cv2.merge([B,G,R])) #Restores the original image
cv2.waitKey(0)


# In[13]:

#Convert an image from RGB to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
for (name, channel) in zip(('B','G','R'), cv2.split(hsv)):
    cv2.imshow(name, channel)
    cv2.waitKey(0)


# In[12]:

#Displaying image in HSV color space
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow('', hsv)
#cv2.waitKey(0)


# In[14]:

#Displaying image in L*a*b color space
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

for (name, channel) in zip(('L*','a*','b*'), cv2.split(lab)):
    cv2.imshow(name, channel)
    cv2.waitKey(0)


# In[ ]:



