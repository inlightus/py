import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/Codecademy/datasets/master/streeteasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

# x_train, t_test, y_train, y_test = train_test_split(x, y, )
# print(list(df.columns))
# ['rental_id', 'rent', 'bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym', 'neighborhood', 'borough'] 

x = df[list(df.columns[2:-2])] # from 'bedrooms' to 'has_gym'
y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state=6)

mlr = LinearRegression()

mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

print(mlr.coef_) # This index are corresponding to df.columns[2:-2]
# according to the coefficients, 'beedrooms', 'building_age_yrs', 'has_roofdeck', and 'has_washer_dryer' have more impacts on the rent than other factors

# sonny_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 0, 1, 0]]
# predict = mlr.predict(sonny_apartment)
# print("Predicted rent: $%.2f" % predict)

plt.scatter(y_test, y_predict, alpha=0.4)

plt.xlabel("Price: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Actual Rent vs Predicted Rent")

plt.show()

# This prediction is more accurate for its lower range of rent 


# This score is better when it is close to 1.0. Score > 0.7 is usually considered good
print("Train score:")
print(mlr.score(x_train, y_train))

print("Test score:")
print(mlr.score(x_test, y_test))

