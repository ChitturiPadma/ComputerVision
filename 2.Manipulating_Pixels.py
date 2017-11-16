
# coding: utf-8

# In[44]:

import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[45]:

img = cv2.imread('/home/padmach/Capabilities/kaggle/Invasive_Species/train/1.jpg')


# In[46]:

(b,g,r)=img[0,25]


# In[4]:

print("Pixel Values: Blue: "+str(b)+" Green: "+str(g)+" Red: "+str(r))


# In[5]:

img[0,25] = (255,255,255)


# In[35]:

#cv2.imshow("Image", img)
#cv2.waitKey(10)
plt.imshow(img)
plt.show()


# In[12]:

img.shape


# In[47]:

(h,w) = img.shape[:2]


# In[48]:

#Cropping the image
(cX, cY) = (w//2, h//2)


# In[6]:

tl = img[0:cY, 0:cX]


# In[7]:

plt.imshow(tl)
plt.show()


# In[9]:

cv2.imshow("Top-Left Corner Image", tl)
cv2.waitKey(20)
#key = cv2.waitKey(5)
#if key == 27:
#    break


# In[8]:

tr = img[0:cY, cX:w]
br = img[cY:h, cX:w]
bl = img[cY:h, 0:cX]


# In[9]:

f, axarr = plt.subplots(2,2)
axarr[0,0] = plt.imshow(tl)
axarr[0,1] = plt.imshow(tr)
axarr[1,0] = plt.imshow(bl)
axarr[1,1] = plt.imshow(br)


# In[10]:

plt.show()


# In[17]:

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(tl)
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(tr)
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(bl)
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(br)


# In[19]:

plt.show()


# In[50]:

#Updating top left region as green
img[0:cY, 0:cX] = (0,0,255)
img[0:cY, cX:w] = (255,0,0)


# In[51]:

plt.imshow(img)


# In[52]:

plt.show()


# In[ ]:



