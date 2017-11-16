
# coding: utf-8

# In[1]:

import cv2
import numpy as np
import imutils


# In[2]:

img = cv2.imread('/home/padmach/data/pyimagesearch/flower3.jpg')


# In[9]:

#Resizing image by width
(h,w) = img.shape[:2]
new_width = 800.0
r = new_width/w
calc_height = h*r
dim = (int(new_width), int(calc_height))
resized_image1 = cv2.resize(img, dim, cv2.INTER_AREA)
cv2.imshow("Image Resized(width)",resized_image1 )
cv2.waitKey(0)


# In[6]:

# Displaying Original image
cv2.imshow('Orginal Image', img)
cv2.waitKey(0)


# In[10]:

# Resizing image by height
new_height = 50
r = new_height/float(h)
calc_width = int(w * r)
dim = (calc_width, new_height)
resized_image2 = cv2.resize(img, dim, cv2.INTER_AREA )
cv2.imshow('Resized image(height)', resized_image2)
cv2.waitKey(0)


# In[11]:

#Resizing image using imutils
resized_image_imutils = imutils.resize(img, width=600)
cv2.imshow('Resized image(width) using imutils', resized_image_imutils)
cv2.waitKey(0)


# In[ ]:



