import matplotlib.pyplot as plt
import numpy as np
import random

rolls = []
for k in range(1000000):
    rolls.append(random.choice([1, 2, 3, 4, 5, 6]))

plt.hist(rolls, bins=np.linspace(0.5, 6.5, 7))

plt.show()