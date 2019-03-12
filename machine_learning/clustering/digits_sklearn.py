import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()

# printing the data
# print(digits.data)
# printing a tuple (# of samples, # of attributes)
# print(digits.data.shape)

n_samples = len(digits.data)
print(n_samples)

# print(digits.images)
# print(digits.target) # answers of the classification for each data
# print(digits.DESCR)

# images_and_labels = list(zip(digits.images, digits.target))
# for index, (image, label) in enumerate(images_and_labels[:10]):
#     plt.subplot(2, 5, index + 1)
#     plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
#     plt.axis('off')
#     plt.title('TrainingL %i' % label)
# plt.show()



# Using Support Vector Machine(SVM)
# C is a degree of amount of accepting classification error
# gammma is a parameter of Gaussian Kernel which determins the vagueness of the borderline
clf = svm.SVC(gamma=0.001, C=100.)

# Training SVM(Using 60% of the datasets)
clf.fit(digits.data[:int(n_samples*6/10)], digits.target[:int(n_samples*6/10)])

expected = digits.target[int(n_samples*-4/10):]
predicted = clf.predict(digits.data[int(n_samples*-4/10):])
print("Classification repot for classifier %s:\n%s\n"
      % (clf, metrics.classification_report(expected, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))


# output with images
images_and_predictions = list(zip(digits.images[int(n_samples*-4/10):], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:12]):
    plt.subplot(3, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)
plt.show()
