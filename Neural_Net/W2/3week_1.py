import numpy as np

x = np.array([2, 1, -1])

W = np.array([[1, 0],[0, 2],[3, 1]])

y = np.dot(x, W)

print("y1 =", y[0])
print("y2 =", y[1])