from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np


temperature = np.array([range(60, 100, 2)])
# print(temperature.shape) # (1, 20)

temperature = temperature.reshape(-1, 1)
# print(temperature.shape) # (20, 1)

sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

plt.plot(temperature, sales, 'o')

model = LinearRegression()
model.fit(temperature, sales)
# print(model.coef_)
# print(model.intercept_)
predicted = model.predict(temperature)
# print(prediction)

plt.plot(temperature, predicted)

plt.show()
