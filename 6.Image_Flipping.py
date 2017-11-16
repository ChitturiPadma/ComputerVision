
# coding: utf-8

# In[1]:

import numpy as np
import cv2
import imutils


# In[2]:

img = cv2.imread('./datasets/flower1.jpg')
cv2.imshow("Original_Image", img)
cv2.waitKey(0)


# In[3]:

#Flipping Horizontally
flip_horizontal = cv2.flip(img, 1)
cv2.imshow("Image_Flipped_Horizontal", flip_horizontal)
cv2.waitKey(0)


# In[4]:

#Flipping Vertically
flip_vertical = cv2.flip(img, 0)
cv2.imshow('Image_Flipped_Vertically', flip_vertical)
cv2.waitKey(0)


# In[5]:

#Flip along both the axes
flip_both = cv2.flip(img, -1)
cv2.imshow("Flip_Both_Axes", flip_both)
cv2.waitKey(0)


# In[ ]:



