import sys, datetime, numpy
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
dataset = sys.argv[1]
limit = int(sys.argv[2])

# Import dataset
total = numpy.genfromtxt(dataset, delimiter=',')
data = total[:limit, 0:-2]
targets = total[:limit, -1]

# Train
rbf = svm.SVC(kernel='rbf')
knn = KNeighborsClassifier()
rbf.fit(data, targets)
knn.fit(data, targets)

# Predict
error_rbf = []
error_knn = []
(points, dimensions) = total.shape
for index in range(limit, points):
  values = total[index, 0:-2]
  correct = total[index, -1]
  output_rbf = rbf.predict(values)
  output_knn = knn.predict(values)
  error_rbf.append(correct - output_rbf)
  error_knn.append(correct - output_knn)
print('Mean Error RBF: ' + str(numpy.mean(error_rbf)))
print('Mean Error KNN: ' + str(numpy.mean(error_knn)))

#  print('Values: ' + str(values))
#  print('Correct: ' + str(correct))
#  print('RBF: ' + str(output_rbf))
#  print('KNN: ' + str(output_knn))
  


