
# coding: utf-8

# In[4]:

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from sklearn.metrics import classification_report
import numpy as np
import matplotlib.pyplot as plt


# In[26]:

losses =[]
epochs = 100
alpha = 0.01
batch_size = 32


# In[5]:

def sigmoid_activation(x):
    return 1.0/(1+np.exp(-x))


# In[6]:

def predict(X, W):
    preds = sigmoid_activation(X.dot(W))
    preds[preds <=0.5] =0 
    preds[preds > 0.5] = 1
    return preds


# In[22]:

def next_batch(X,y,batchSize ):
    for i in np.arange(0, X.shape[0], batchSize):
        yield(X[i:i+batchSize], y[i:i+batchSize])


# In[7]:

(X,y) = make_blobs(centers=2, cluster_std=1.5, n_features=2, n_samples=1000, random_state=1)


# In[10]:

X = np.c_[X, np.ones(X.shape[0])]


# In[13]:

y = y.reshape(y.shape[0],1)


# In[15]:

(trainX, testX, trainY, testY) = train_test_split(X,y, test_size=0.5, random_state=42)


# In[20]:

W = np.random.rand(X.shape[1],1)


# In[28]:

for epoch in np.arange(0, epochs):
    epochLoss = []
    
    for(batchX, batchY) in next_batch(X,y, batch_size):
        preds = sigmoid_activation(batchX.dot(W))
        
        error = preds - batchY
        loss = np.sum(error**2)
        epochLoss.append(loss)
        
        gradient = batchX.T.dot(error)
        W += -alpha * gradient
    original_loss = np.average(epochLoss)
    losses.append(original_loss)
    
    if epoch ==0 or (epoch+1)%5 ==0:
        print("[INFO] epoch={}, loss={:.7f}".format(int(epoch+1), loss))


# In[29]:

print("[INFO] Evaluating...")
preds = predict(testX, W)
print(classification_report(testY, preds))


# In[30]:

plt.style.use("ggplot")
plt.figure()
plt.title("Data")
plt.scatter(testX[:,0], testX[:, 1], marker='o', c=testY, s=30)

plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, epochs), losses)
plt.title("Training Loss")
plt.xlabel("Epoch#")
plt.ylabel("Loss")
plt.show() #using SGD, loss is more smooth.


# In[ ]:



