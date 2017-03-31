import numpy as np

x = np.random.random(10)

print(np.any(x > 0.9))

print(np.all(x >= 0.1))

print(x)