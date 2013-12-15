"""
Support Vector Machines
"""
import numpy as np
from sklearn import datasets
from sklearn import svm
import pylab as pl

# Load dataset
iris = datasets.load_iris()

# Create support vector classifiers
svc_linear = svm.SVC(kernel='linear') # LINEAR
svc_poly = svc = svm.SVC(kernel='poly', degree=3) # POLYNOMIAL
svc_rbf = svm.SVC(kernel='rbf') # RADIAL BASIS FUNCTION

# Train model
svc_linear.fit(iris.data, iris.target)   
svc_poly.fit(iris.data, iris.target)
svc_rbf.fit(iris.data, iris.target)  

# Generate random data
iris.random = np.random.random([10,4])*5
print(iris.random)

# Predict classification
result_linear = svc_linear.predict(iris.random) 
result_poly = svc_poly.predict(iris.random) 
result_rbf = svc_rbf.predict(iris.random)
print(str(result_linear))
print(str(result_poly))
print(str(result_rbf))
