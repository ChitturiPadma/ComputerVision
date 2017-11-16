
# coding: utf-8

# In[4]:

import numpy as np
import cv2
import imutils


# In[5]:

#Reading input image
img = cv2.imread('/home/padmach/data/pyimagesearch/flower3.jpg')
img.shape


# In[6]:

#Crop the image
cropped_image1 = img[20:220, 20:220] #manually supplying numpy array slices to crop the image [y:EndY, x:EndX]
cv2.imshow('Cropped_Image', cropped_image1)
cv2.waitKey(0)


# In[ ]:



