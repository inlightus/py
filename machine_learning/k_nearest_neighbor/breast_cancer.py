import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_breast_cancer

dataset = load_breast_cancer()
# print([i for i in dataset])
# print(dataset.data)
# print(dataset.target)
# print(dataset.target_names)
# print(dataset.DESCR)
# print(dataset.feature_names)

training_data, validation_data, training_labels, validation_labels = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=100)

accuracies = []

for k in range(1, 101):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(training_data, training_labels)

    accuracies.append(classifier.score(validation_data, validation_labels))

k_list = range(1, 101)

plt.plot(k_list, accuracies)
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")

plt.show()
