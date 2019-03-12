import numpy as np

w1 = np.random.randn(2, 4) # weight
b1 = np.random.randn(4) # bias
x = np.random.randn(10, 2) # input
h = np.dot(x, w1) + b1

print(w1)
print(b1)
print(x)
print(h)
