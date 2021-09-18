#!/usr/bin/env python
# coding: utf-8

# In[10]:


#importing related modules and libraries
import pandas as pd
from matplotlib import pyplot  as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score
from matplotlib.colors import ListedColormap
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import sklearn.model_selection as ms
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D


# In[6]:


#importing data
data=pd.read_csv('heart.csv')

#Defining input and output variables X and y
X=data.iloc[:, 1:-1]
y=data.iloc[:, -1]

#initiating the KNN algorithm
knn = KNeighborsClassifier()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Selecting the value of k using cross validation method
k_neighbours = list(range(1,21,2))
n_grid = [{'n_neighbors': k_neighbours}]
cv_knn = GridSearchCV(estimator=knn,param_grid=n_grid,cv=ms.KFold(n_splits=10))
cv_knn.fit(X_train, y_train)
best_k = cv_knn.best_params_['n_neighbors']

#Printing the classification report
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print('Confusion matric: \n',confusion_matrix(y_test,y_pred),'\n')
print('Classification report: \n\n',classification_report(y_test, y_pred))


# In[9]:


#Data visualisation
plt.figure()
sns.pairplot(data.iloc[:,[0,2,3,4,7,9,-1]], hue = 'target', markers=["X", "o"])
plt.show()


# In[11]:


get_ipython().run_line_magic('matplotlib', 'notebook')

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot( projection = '3d', )

x = data['thalach']
y = data['trestbps']
z = data['chol']

ax.set_xlabel("maximum heart rate achieved")
ax.set_ylabel("resting blood pressure")
ax.set_zlabel("serum cholestoral in mg/dl")

ax.scatter(x, y, z, c=data['target'], cmap="viridis")

plt.show()


# In[ ]:




