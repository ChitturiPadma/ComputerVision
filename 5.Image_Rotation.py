
# coding: utf-8

# In[29]:

import numpy as np
import cv2
import imutils


# In[2]:

img = cv2.imread('/home/padmach/data/pyimagesearch/flower3.jpg')


# In[5]:

(h,w) = img.shape[:2]


# In[6]:

(cX,cY) =(w/2, h/2)


# In[21]:

'''getRotationMatrix2D takes 3 arguments -  point about which we want to rotate, angle and scale (resizes the image)'''
rot_matrix1 = cv2.getRotationMatrix2D((cX,cY),45,0.5) #center, angle and scale, rotates in counter clockwise direction
rot_image1 = cv2.warpAffine(img, rot_matrix1,(w,h))
cv2.imshow("Rotated_Image by 45 degrees",rot_image1)
cv2.waitKey(0)


# In[19]:

'''rotates by 90 degress in clockwise  direction and scale 2.0 zooms the image'''

rot_matrix2 = cv2.getRotationMatrix2D((cX, cY), -90, 2.0) 
rot_image2 = cv2.warpAffine(img, rot_matrix2,(w,h))
cv2.imshow("Rotated by 90 degrees", rot_image2)
cv2.waitKey(0)


# In[27]:

#Rotating about an arbitrary point
rot_matrix3 = cv2.getRotationMatrix2D((cX-50, cY-50), 60,1.0)
rot_image3 = cv2.warpAffine(img, rot_matrix3,(w,h))
cv2.imshow('Rotated image by 60 degrees',rot_image3)
cv2.waitKey(0)


# In[28]:

rot_image3.shape


# In[31]:

#Rotate an image using imutils
rotated_image_imutils = imutils.rotate(img, 30, (cX, cY),1.0)
cv2.imshow("Rotated image by 30 degrees", rotated_image_imutils)
cv2.waitKey(0)


# In[ ]:



