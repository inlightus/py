# K-Nearest Neighbor Algorithm
# 1. Normalize the data
# 2. Find the k nearest neighbors
# 3. Classify the new point based on those neighbors

# distance function
def distance(a, b):
    distance = 0
    for x, y in zip(a, b):
        distance += (x - y) ** 2
    return distance ** 0.5

def min_max_normalize(lst):
    minimum = min(lst)
    maximum = max(lst)
    normalized = []

    for value in lst:
        normalized_num = (value - minimum) / (maximum - minimum)
        normalized.append(normalized_num)

    return normalized


# Using sklearn

from sklearn.neighbors import KNeighborsClassifier(n_neighbours=5)
classifier.fit(dataset, labels)
guess = classifier.predict(target)


