
# coding: utf-8

# In[2]:

import numpy as np
import cv2


# In[3]:

import matplotlib.pyplot as plt
import argparse


# In[4]:

ap = argparse.ArgumentParser()


# In[5]:

ap.add_argument("-i", "--image", required=True, help="path of the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Image", image)
cv2.waitKey(5)


# In[ ]:



