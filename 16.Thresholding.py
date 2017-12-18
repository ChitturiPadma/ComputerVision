
# coding: utf-8

# In[50]:

import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[51]:

img = cv2.imread('/home/padmach/data/pyimagesearch/flower3.jpg')
#cv2.imshow('', img)
#cv2.waitKey(0)


# In[52]:

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3,3),0)
#cv2.imshow('', blurred)
#cv2.waitKey(0)


# In[53]:

#Apply inverse thresholding; pixel value > T set to 0 and pixel value < T set to 255
#T = 200 # threshold value
(T, threshInv) = cv2.threshold(blurred, 110, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Threshold Binary Inverse', threshInv)
cv2.waitKey(0)


# In[54]:

#Apply Normal thresholding
(T, thresh) = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh)
cv2.waitKey(0)


# In[49]:

#Visualize masked regions in the image
cv2.imshow('Output', cv2.bitwise_and(img, img, mask= threshInv))
cv2.waitKey(0)


# In[56]:

#Appling Otsu's method of thresholding
(T_otsu, threshInvOtsus) = cv2.threshold(blurred, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('Threshold Otsu', threshInvOtsus)
cv2.waitKey(0)


# In[57]:

print('Otsus thresholding value {}'.format(T_otsu))


# In[58]:

#Visualize the masjed regions 
cv2.imshow('Masked Region Otsu thresholding', cv2.bitwise_and(img, img, mask=threshInvOtsus))
cv2.waitKey(0)


# In[64]:

license_plate = cv2.imread('/home/padmach/data/pyimagesearch/adaptive_threhsold_license_plate.png')
gray_license_plate = cv2.cvtColor(license_plate, cv2.COLOR_BGR2GRAY)
license_blurred = cv2.GaussianBlur(gray_license_plate, (3,3),0)
(T_license_otsu, license_threshold_otsu) = cv2.threshold(license_blurred, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('License plate using Otsu', license_threshold_otsu)
cv2.waitKey(0)


# In[65]:

#Final output of visualizing the license plate
cv2.imshow('Output', cv2.bitwise_and(license_plate, license_plate, mask=license_threshold_otsu))
cv2.waitKey(0)


# In[63]:

#Applying adaptiveThreshold
#adaptive threshold achieves better results
thresh_adaptive = cv2.adaptiveThreshold(license_blurred,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,25,15)
cv2.imshow('Adaptive Threshold Image', thresh_adaptive)
cv2.waitKey(0)


# In[ ]:



