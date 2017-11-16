
# coding: utf-8

# In[19]:

import cv2
import numpy as np
import imutils


# In[3]:

img = cv2.imread('/home/padmach/data/pyimagesearch/flower3.jpg')


# In[4]:

translation_matrix = np.float32([[1,0,25],[0,1,50]])


# In[5]:

#Shifting right by 25 pixels and down by 50 pixels
shifted_img = cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))


# In[7]:

cv2.imshow('Shifted_Image', shifted_img)
cv2.waitKey(0)


# In[17]:

#Shifting by left 50 pixels and up by 90 pixels
translation_matrix2 = np.array([[1,0,-50],[0,1,-90]], dtype='float') #type 'float is mandatory for translation matrix
shifted_img2 = cv2.warpAffine(img, translation_matrix2, (img.shape[1], img.shape[0]))
cv2.imshow('Shifted_Image_new', shifted_img2)
cv2.waitKey(0)


# In[13]:

translation_matrix.dtype


# In[18]:

translation_matrix2.dtype


# In[20]:

shifted_imutils_image = imutils.translate(img,0,100)


# In[21]:

cv2.imshow("Translated_image", shifted_imutils_image)
cv2.waitKey(0)


# In[ ]:



