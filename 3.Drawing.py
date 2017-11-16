
# coding: utf-8

# In[5]:

import cv2
import numpy as np


# In[6]:

canvas = np.zeros((300,300,3), dtype='uint8')
green = (0, 255, 0) #BGR format
red = (0,0,255) #BGR format
blue = (255, 0, 0) #BGR format


# In[7]:

#Drawing Lines
cv2.line(canvas, (0,0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#cv2.imwrite('/home/padmach/imagee.jpg',canvas)


# In[9]:

cv2.line(canvas,(0,300),(300,300),blue)
cv2.imshow("Canvas1", canvas)
cv2.waitKey(0)


# In[10]:

# draw a 3 pixel thick red line from the top-right corner to the bottom left
cv2.line(canvas, (300,0),(0,300), red, 3)
cv2.imshow('Canvas2', canvas)
cv2.waitKey(0)


# In[11]:

#Drwaing Rectangles

cv2.rectangle(canvas, (10,10),(60,60), green)
cv2.imshow('Canvas_Rectangle', canvas)
cv2.waitKey(0)


# In[16]:

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5) #5 indicates thickness
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# In[15]:


cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1) #-1 as thickness, rectangle is drawn with color filled.
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# In[14]:


cv2.rectangle(canvas, (200, 50), (225, 125), blue, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# In[22]:

#Drawing Circles
canvas_new = np.zeros((300, 300,3), dtype='uint8')
(center_x, center_y) = (canvas_new.shape[1]/2, canvas_new.shape[0]/2)
for r in range(0,175,25):
    cv2.circle(canvas_new, (center_x, center_y), r, red, 5) #r is radius, red is the color and 5 is the thickness


# In[23]:

cv2.imshow("Canvas_Circle", canvas_new)
cv2.waitKey(0)


# In[30]:

#Abstract drawing
canvas_new2 = np.zeros((300,300,3),dtype='uint8')
for r in range(0,25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high = 256, size=(3,))
    point = np.random.randint(0,high = 300, size = (2,))
    
    cv2.circle(canvas_new2, tuple(point), radius, color, -1)
cv2.imshow("Abstract_Drawing", canvas_new2)
cv2.waitKey(0)


# In[25]:

np.random.randint(0, high=300, size=(2,))


# In[32]:

#Drawing on existing image
img = cv2.imread('./datasets/flower1.jpg')

cv2.circle(img, (img.shape[1]/2, img.shape[0]/2), 25, (0,255,0), 2)
cv2.rectangle(img, (10,10),(60,60), (0,0,255),-1)
cv2.line(img, (200,0),(150,200),(255,0,0),3)

cv2.imshow('Custom_Image', img)
cv2.waitKey(0)


# In[ ]:



