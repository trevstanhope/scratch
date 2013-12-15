# Modules
import sys, datetime, numpy
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import warnings
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# Arguments
data_file = sys.argv[1]
target_file = sys.argv[2]
limit = int(sys.argv[3])

# Import dataset
data_set = numpy.genfromtxt(data_file, delimiter=',')
target_set = numpy.genfromtxt(target_file, delimiter=',')
(target_p, target_d) = target_set.shape
(data_p, data_d) = data_set.shape
print data_set.shape
print target_set.shape

# Predict
with warnings.catch_warnings():
  warnings.simplefilter("ignore")
  for interval in range(target_d):
    print('Calculating Interval: ' + str(interval))
    knn = KNeighborsClassifier()
    knn.fit(data_set[:limit, :], target_set[:limit, interval]) # train with values up to limit
    rbf = svm.SVC(kernel='rbf')
    rbf.fit(data_set[:limit, :], target_set[:limit, interval]) # train with values up to limit
    error_knn = []
    error_rbf = []
    for index in range(limit, data_p):
      values = data_set[index, :]
      correct = target_set[index, interval]
      output_knn = knn.predict(values)
      output_rbf = rbf.predict(values)
      error_rbf.append(correct - output_knn)
      error_knn.append(correct - output_rbf)
    print('\tKNN Mean Error: ' + str(numpy.mean(error_knn)))
    print('\tRBF Mean Error: ' + str(numpy.mean(error_rbf)))  
