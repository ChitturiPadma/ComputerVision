
# coding: utf-8

# In[41]:

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np


# In[42]:

def sigmoid_activation(x):
    return 1.0/(1+np.exp(-x))


# In[43]:

def predict(X, W):
    preds = sigmoid_activation(X.dot(W))
    
    preds[preds <=0.5] = 0
    preds[preds >0] =1
    
    return preds


# In[44]:

(X,y) = make_blobs(n_samples=1000,n_features=2, cluster_std=1.5, random_state=1, centers=2)


# In[45]:

y = y.reshape(y.shape[0],1)


# In[46]:

X = np.c_[X, np.ones(X.shape[0])]


# In[47]:

(trainX, testX, trainY, testY) = train_test_split(X, y, test_size = 0.5, random_state = 42)


# In[55]:

print("[INFO] Training...")


# In[49]:

W = np.random.rand(X.shape[1], 1)
losses = []


# In[50]:

epochs = 100
alpha = 0.01


# In[51]:

for epoch in np.arange(0, epochs):
    preds = sigmoid_activation(trainX.dot(W))
    
    error = preds - trainY
    loss = np.sum(error**2)
    losses.append(loss)
    
    gradient = trainX.T.dot(error) # gradient in the dot product between data pointx X and the error.
    W += -alpha * gradient #updating the weights by taking step in the -ve direction of the gradient
    
    if epoch ==0 or (epoch+1)%5 ==0:
        print("[INFO] epoch = {}, loss={:.7f}".format(int(epoch+1), loss))


# In[52]:

print("[INFO] Evaluating...")
preds = predict(testX, W)
print(classification_report(testY, preds))


# In[54]:

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
plt.show()


# In[ ]:



