
# coding: utf-8

# In[1]:

import cv2
import numpy as np
import imutils


# In[15]:

img = cv2.imread('./datasets/flower3.jpg')
logo_img = cv2.imread('./datasets/pyimagesearch_logo_github.png')
car_img = cv2.imread('./datasets/licence_plate1.jpg')
gray_car = cv2.cvtColor(car_img, cv2.COLOR_BGR2GRAY)

car_img_light = cv2.imread('./datasets/licence_plate2.jpg')
gray_car_light = cv2.cvtColor(car_img_light, cv2.COLOR_BGR2GRAY)

car_img_blue = cv2.imread('./datasets/licence_plate3.jpg')
gray_car_blue = cv2.cvtColor(car_img_blue, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Original Image",img)
#cv2.waitKey(0)


# In[3]:

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_logo = cv2.cvtColor(logo_img, cv2.COLOR_BGR2GRAY)
#eroded = cv2.erode(gray, None, iterations=2)
#cv2.imshow("Eroded image", eroded)
#cv2.waitKey(0)


# In[61]:

eroded_new = cv2.erode(gray, None, 30)


# In[62]:

#Eroding a grayscale image
for i in range(0,10):
    eroded = cv2.erode(gray, None, iterations = i)
    cv2.imshow("Eroded {} times".format(i+1), eroded)
    cv2.waitKey(0)


# In[49]:

cv2.imshow('Eroded One time', eroded_new)
cv2.waitKey(0)


# In[59]:

#Dilating an image
for i in range(0,30):
    dilated = cv2.dilate(img, None, iterations = i)
    cv2.imshow("Dilated Image", dilated)
    cv2.waitKey(0)


# In[68]:

# Opening operation - Erosion followed by dilation
kernelSizes = [(3,3),(5,5),(7,7), (9,9),(11,11),(13,13)]
for kernelSize in kernelSizes:
    kernel_structuring = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opened_image = cv2.morphologyEx(gray_logo, cv2.MORPH_OPEN, kernel_structuring)
    cv2.imshow("Opening: ({}, {})".format(kernelSize[0], kernelSize[1]), opened_image)
    cv2.waitKey(0)


# In[69]:

#Closing operation - dialtion followed by erosion
kernelSizes = [(3,3),(5,5),(7,7),(9,9),(11,11),(13,13)]
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closed_image = cv2.morphologyEx(gray_logo, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closed image", closed_image)
    cv2.waitKey(0)


# In[4]:

#morphological gradient - difference between dilation and erosion
#morphological gradient revelas the outline of the image
kernelSizes = [(3,3),(5,5),(7,7)]
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray_logo, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(kernelSize[0], kernelSize[1]), gradient)
    cv2.waitKey(0)


# In[10]:

#Top hat operator - detect bright objects against dark background 
#Tophat is the difference between input image and the opening 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13,5)) # since license plat is 3 times wider than it is tall

# As the color of the car is dark, detecting license plate was easier.
tophat = cv2.morphologyEx(gray_car, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Tophat", tophat)
cv2.waitKey(0)


# In[11]:

#Black hat operation - difference between closing of the input image and input image itself
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13,5))
blackhat = cv2.morphologyEx(gray_car_light, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('Black Hat', blackhat)
cv2.waitKey(0)


# In[19]:

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13,5))
blackhat = cv2.morphologyEx(gray_car_blue, cv2.MORPH_BLACKHAT, kernel)
tophat = cv2.morphologyEx(blackhat, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('License Plate', tophat)
cv2.waitKey(0)


# In[ ]:



