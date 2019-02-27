import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


diabetes = load_diabetes()
# print(diabetes)
# print([i for i in diabetes])
# print(diabetes.data)
# print(diabetes.target)
# print(diabetes.feature_names)
# print(diabetes.DESCR)

df = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)
# print(df)

X = df[['age']]
diabetes_age_train, diabetes_age_test, diabetes_y_train, diabetes_y_test = train_test_split(X, diabetes.target, test_size=0.2)

model = LinearRegression()
model.fit(diabetes_age_train, diabetes_y_train)
predicted = model.predict(diabetes_age_test)

print("Coefficients: ", model.coef_)
print("Standard Deviation: %.2f" % mean_squared_error(diabetes_y_test, predicted))
print("Score: %.2f" % r2_score(diabetes_y_test, predicted))

plt.scatter(diabetes_age_train, diabetes_y_train, alpha=0.4)
plt.plot(diabetes_age_test, predicted, color="orange")

plt.title("Diabetes Dataset")
plt.xlabel("Age")
plt.ylabel("Quantitative Measure of Disease Progression One Year After")
plt.show()
