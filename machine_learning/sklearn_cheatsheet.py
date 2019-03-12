# Scikit-Learn CheatSheet

# Linear Regression
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_training_data, y_training_data)
model.coef_ # .coef_ contains the coefficients
model.intercept_ #.intercept_ contains the intercept

predictions = model.predict(x_data)
predictions.score() # .score() returns the coefficients of determination R2


# Naive Bayes
from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()

model.fit(x_training_data, y_training_data)

predictions = model.predict(x_data)
probabilities = model.predict_proba(x_data)


# K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()

model.fit(x_training_data, y_training_data)

predictions = model.predict(x_data)
probabilities = model.predict_proba(x_data)


# K-Means
from sklearn.cluster import KMeans

model = KMeans(n_clusters=4, init='random')

# n_clusters: number of clusters to form and number of centroids to generate
# init: method for initialization
# random_state: the seed used by the random number generator


model.fit(x_training_data)
predictions = model.predict(x_data)


# Validating the Model
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

print(accuracy_score(true_labels, guesses))
print(recall_score(true_labels, guesses))
print(precision_score(true_labels, guesses))
print(f1_score(true_labels, guesses))

from sklearn.metrics import confusion_matrix

print(confusion_matrix(true_labels, fuesses))


# Training Sets and Test Sets
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)


