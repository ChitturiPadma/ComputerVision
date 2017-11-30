
# coding: utf-8

# In[54]:

from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths
import imutils
import cv2
import numpy as np


# In[55]:

class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        self.width = width
        self.height = height
        self.inter = inter
        
    def preprocess(self, image):
        return cv2.resize(image, (self.width, self.height))


# In[56]:

class SimpleDatasetLoader:
    def __init__(self, preprocessors=None):
        self.preprocessors = preprocessors
        
        if self.preprocessors is None:
            self.preprocessors=[]
    def load(self, imagePaths, verbose = -1):
        data = []
        labels = []
        for (i, imagePath) in enumerate(imagePaths):
            image = cv2.imread(imagePath)
            label = imagePath.split(os.path.sep)[-2]
            
            if self.preprocessors is not None:
                for p in self.preprocessors:
                    image = p.preprocess(image)
                    #print(image.shape)
            data.append(image)
            labels.append(label)
            
            if verbose > 0 and i>0 and (i+1)%verbose==0:
                print("[INFO] processed {}/{}".format(i+1, len(imagePaths)))
        return(np.array(data), np.array(labels))


# In[57]:

image_paths = list(paths.list_images('/home/padmach/data/DogVsCats/train'))


# In[58]:

sp = SimplePreprocessor(32, 32)
sdl = SimpleDatasetLoader(preprocessors=[sp])
(data, labels) = sdl.load(image_paths, verbose=500)


# In[60]:

data = data.reshape((data.shape[0], 3072))


# In[63]:

le = LabelEncoder()
labels = le.fit_transform(labels)


# In[70]:

(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size = 0.25, random_state=42)


# In[73]:

model = KNeighborsClassifier(n_neighbors=2)
model.fit(trainX, trainY)


# In[74]:

print(classification_report(testY, model.predict(testX),target_names=le.classes_))


# In[ ]:



