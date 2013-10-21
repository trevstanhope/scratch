#!/usr/bin/env python
from sklearn import datasets
import pylab as pl 
import time

# Iris
iris = datasets.load_iris()
print(iris.data.shape)
print(iris.target.shape)

# Digits
digits = datasets.load_digits()
print(digits.data.shape)
print(digits.target.shape)
