# functions used for Logistic Regression
import numpy as np

def log_odds(features, coefficients, intercept):
    return np.dot(features, coefficients) + intercept


def sigmoid(z):
    denominator = 1 + np.exp(-z)
    return 1 / denominator


def log_loss(probabilities, actual_class):
    return np.sum(-(1/actual_class.shape[0])*(actual_class*np.log(probabilities) + (1-actual_class)*np.log(1-probabilities)))



