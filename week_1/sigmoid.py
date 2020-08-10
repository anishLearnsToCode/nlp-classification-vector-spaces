import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(np.negative(z)))


# print(sigmoid([0, 1, 2, 3, 4, 5]))

a = np.array([0, 1, 2])
print(a.shape)
print(a.transpose().shape)
