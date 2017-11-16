
# coding: utf-8

# In[1]:

import cv2
import numpy as np
import imutils


# In[2]:

'''Using OpenCV, addition/subtraction of images performs clipping i.e. values falling outside the range [0,255]
are clipped'''
img = cv2.imread('/home/padmach/data/pyimagesearch/flower1.jpg')
matrix = np.ones(img.shape, dtype='uint8')*100
added_image = cv2.add(img,matrix)
cv2.imshow('Added_Image', added_image)
cv2.waitKey(0)


# In[3]:

#Subtracting the images
matrix2 = np.ones(img.shape,dtype='uint8')*50
subtract_image = cv2.subtract(img, matrix2)
cv2.imshow('Subtracted_Image', subtract_image)
cv2.waitKey(0)


# In[ ]:

'''In case of adding 2 numpy arrays using np.sum, if a value falls outside 255 let's say 260, the value
will be wrapped around which would be 5 '''

