
# coding: utf-8

# In[11]:

import cv2
import numpy as np


# In[27]:

orig = cv2.imread('/home/padmach/data/DogVsCats/train/dog/dog.63.jpg')
image = cv2.resize(orig, (32,32)).flatten()


# In[28]:

'''
cv2.imshow('Resized', image)
cv2.waitKey(0)
'''


# In[29]:

labels = ['dog','cat','panda']
np.random.seed(1)


# In[30]:

W = np.random.rand(3, 3072)
b = np.random.rand(3)


# In[31]:

scores = W.dot(image)+b


# In[34]:

for (label, score) in zip(labels, scores):
    print("[INFO] {}: {:.2f}".format(label, score))

cv2.putText(orig, "Label: {}".format(labels[np.argmax(scores)]),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


# In[35]:

cv2.imshow("Image", orig)
cv2.waitKey(0)


# In[36]:




# In[ ]:



