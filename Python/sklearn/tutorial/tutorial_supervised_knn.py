#!/usr/bin/env python
"""
NearestNeighbor
http://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html
"""
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris = datasets.load_iris()
knn = KNeighborsClassifier()
knn.fit(iris.data, iris.target) # train model
iris.random = np.random.random([1,4])*10
print(iris.random)
result = knn.predict(iris.random) 
print(result)
