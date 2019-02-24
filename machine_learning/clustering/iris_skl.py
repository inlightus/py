import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn import datasets
from sklearn.cluster import KMeans

# Step1: use KMeans() method to build a model that finds k clusters
model = KMeans(n_clusters=3)

# importing datasets from sklearn
iris = datasets.load_iris()
samples = iris.data

target = iris.target

# Use KMeans() to create a model that finds 3 clusters
model = KMeans(n_clusters=3)

# Use .fit() to fit the model to samples
model.fit(samples)

# Use .predict() to determine the labels of samples
labels = model.predict(samples)

# predicting the new samples
new_samples = np.array([[5.7, 4.4, 1.5, 0.4], [6.5, 3. , 5.5, 0.4], [5.8, 2.7, 5.1, 1.9]])

result = model.predict(new_samples)

# Choosing sample colums we want to categorize
x = samples[:, 0]
y = samples[:, 1]

# color is auto-selected by labels
plt.scatter(x, y, c=labels, alpha=0.5)

plt.xlabel('sepal length(cm)')
plt.ylabel('sepal width(cm)')

plt.show()

# cross-tabulation by using pandas
species = np.chararray(target.shape, itemsize=150)

for i in range(len(samples)):
    if target[i] == 0:
        species[i] = 'setosa'
    elif target[i] == 1:
        species[i] = 'versicolor'
    elif target[i] == 2:
        species[i] = 'virginica'

df = pd.DataFrame({'labels':labels, 'species':species})

ct = pd.crosstab(df['labels'], df['species'])
print(ct)


# The number of appropriate clusters calculated by Inertia
num_clusters = list(range(1, 9))
inertias = []

for k in num_clusters:
    model = KMeans(n_clusters=k)
    model.fit(samples)
    inertias.append(model.inertia_)

plt.plot(num_clusters, inertias, '-o')

plt.xlabel('Number of Clusters(k)')
plt.ylabel('Inertia')

plt.show()
