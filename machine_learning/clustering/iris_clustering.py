import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from copy import deepcopy

iris = datasets.load_iris()

# print(iris.data)
# print(iris.target)
# print(iris.DESCR)

samples = iris.data

x = samples[:, 0]
y = samples[:, 1]

sepal_length_width = np.array(list(zip(x, y)))

# Place K random centroids
# K is the number of clusters we expect
k = 3

centroids_x = np.random.uniform(min(x), max(x), size=k)
centroids_y = np.random.uniform(min(y), max(y), size=k)
centroids = np.array(list(zip(centroids_x, centroids_y)))


def distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

# initializeing the result set
centroids_old = np.zeros(centroids.shape)
labels = np.zeros(len(samples))
distances = np.zeros(k)
error = np.zeros(k)

error = [distance(centroids[i], centroids_old[i]) for i in range(k)]
# error[0] = distance(centroids[0], centroids_old[0])
# error[1] = distance(centroids[1], centroids_old[1])
# error[2] = distance(centroids[2], centroids_old[2])
#

# the error will be distances between centroids and old_centroids
while all(error) != 0:

    for i in range(len(samples)):
        distances = [distance(sepal_length_width[i], centroids[j]) for j in range(k)]
        cluster = np.argmin(distances)
        labels[i] = cluster

    centroids_old = deepcopy(centroids)

# taking the mean of each label to get a new centroids
    for i in range(k):
        points = [sepal_length_width[j] for j in range(len(sepal_length_width)) if labels[j] == i]
        centroids[i] = np.mean(points, axis=0)

    error = [distance(centroids[i], centroids_old[i]) for i in range(k)]

colors = ['r', 'g', 'b']

for i in range(k):
    points = np.array([sepal_length_width[j] for j in range(len(samples)) if labels[j] == i])
    plt.scatter(points[:, 0], points[:, 1], c=colors[i], alpha=0.5)

print(centroids)


plt.scatter(centroids[:, 0], centroids[:, 1], marker='D', s=150)

plt.xlabel("sepal length(cm)")
plt.ylabel("sepal width(cm)")

plt.show()
