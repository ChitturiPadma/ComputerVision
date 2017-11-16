
# coding: utf-8

# In[1]:

import cv2
import numpy as np
import imutils
import argparse


# In[2]:

img = cv2.imread('./datasets/flower3.jpg')
cv2.imshow("Original_Image", img)
cv2.waitKey(0)


# In[3]:

#Splitting RGB components of an image
#Individual channel investigation hepls in understanding edge detection and thresholding

(B, G, R) = cv2.split(img) # as RGB image is stored in reverse channel order
#Showing individual channels in grayscale format
cv2.imshow("Red_Component", R)
cv2.imshow('Blue_Component', B)
cv2.imshow('Green_Component', G)
cv2.waitKey(0)


# In[4]:

#Merging the channels back
merged = cv2.merge([B, G, R])
cv2.imshow("Merged_Image", merged)
cv2.waitKey(0)


# In[5]:

#Merging the channels in reverse order - changes the color component of original image
cv2.imshow("Merged_Image2", cv2.merge([R, G, B]))
cv2.waitKey(0)


# In[8]:

#Visualize each channel in its corresponding color
zeros = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow("Red", cv2.merge([zeros, zeros, R])) 
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)


# In[ ]:



