
# coding: utf-8

# In[1]:

#Extract non-rectangular regions of interest (ROI)
import cv2
import numpy as np
import imutils


# In[2]:

#Draw a rectangle
canvas1  = np.zeros((300,300), dtype='uint8')
rectangle = cv2.rectangle(canvas1, (25, 25),(275, 275),255,-1)
cv2.imshow('Rectangle', rectangle) #Binary imagei
cv2.waitKey(0)


# In[3]:

canvas2  = np.zeros((300,300), dtype='uint8')
circle = cv2.circle(canvas2, (150,150), 150,255,-1)
cv2.imshow('Circle', circle) #Binary Image
cv2.waitKey(0)


# In[4]:

#Bitwise AND - examine both pixels and if both > 0 then the pixel is turned ON and set to 255
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow('AND', bitwiseAnd)
cv2.waitKey(0)


# In[5]:

#Bitwise OR - extract if either of the pixels is > 0 and output pixel is set to 255
bitWiseOR = cv2.bitwise_or(rectangle, circle)
cv2.imshow('OR', bitWiseOR)
cv2.waitKey(0)


# In[6]:

#Bitwise XOR- both the pixels should not have value > 0 
bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
cv2.imshow('XOR', bitwiseXOR)
cv2.waitKey(0)


# In[7]:

#Bitwise NOT - invert the values of pixel values
bitwiseNOT = cv2.bitwise_not(rectangle)
cv2.imshow('NOT', bitwiseNOT)
cv2.waitKey(0)

bitwiseNOT2 = cv2.bitwise_not(circle)
cv2.imshow('NOT', bitwiseNOT2)
cv2.waitKey(0)


# In[12]:




# In[ ]:



