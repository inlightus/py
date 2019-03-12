import numpy as np

class activationFunction():


    def step(self, x):
        return np.array(x > 0, dtype=np.int)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def relu(self, x):
        return np.maximum(0, x)


