"""
"""
from sklearn import cluster, datasets
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target
pca = decomposition.PCA()
pca.fit(iris_X)
X_reduced = pca.fit_transform(X)
