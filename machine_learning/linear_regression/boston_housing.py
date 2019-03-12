import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

boston = load_boston()
# print([i for i in boston])
# print(boston.data) # the data to learn
# print(boston.target) # the regression targets
# print(boston.feature_names)
# print(boston.DESCR)

df = pd.DataFrame(boston.data, columns = boston.feature_names)
# print(df)

# Set the x-values to the nitrogen oxide concentration:
X = df[['NOX']]
boston_nox_train, boston_nox_test, boston_y_train, boston_y_test = train_test_split(X, boston.target, test_size=0.2)


# Y-values are the prices:
y = boston.target

model = LinearRegression()
model.fit(X, y)
predicted = model.predict(X)

plt.scatter(X, y, alpha=0.4)
plt.plot(X, predicted, color="orange")

plt.title("Boston Housing Dataset")
plt.xlabel("Nitric Oxides Concentration")
plt.ylabel("House Price ($)")

plt.show()
