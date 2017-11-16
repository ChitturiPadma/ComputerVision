
# coding: utf-8

# In[4]:

import cv2
import numpy as np
import argparse
import imutils


# In[13]:

#Reading the input image
img = cv2.imread('./datasets/flower3.jpg')
cv2.imshow('Original_Image',img)
cv2.waitKey(0)


# In[14]:

#Extract ROI using cropping or masking
mask = np.zeros(img.shape[:2], dtype='uint8')
cv2.rectangle(mask, (0,20),(200, 300), 255, -1)
cv2.imshow("Zeros_Image", mask)
cv2.waitKey(0)


# In[17]:

#Applying Mask
masked = cv2.bitwise_and(img, img,mask=mask)#bitwise_and is used to apply mask to the images
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)


# In[18]:

#Applying non-rectangular mask
mask_circle = np.zeros(img.shape[:2], dtype='uint8')
cv2.circle(mask_circle, (145, 200), 100, 255, -1)
cv2.imshow("Circle Mask", mask_circle)
cv2.waitKey(0)


# In[19]:

masked_non_rectangle = cv2.bitwise_and(img, img, mask=mask_circle)
cv2.imshow("Circle Mask Applied to Image", masked_non_rectangle)
cv2.waitKey(0)


# In[ ]:



