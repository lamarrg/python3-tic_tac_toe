import matplotlib.pyplot as plt
import numpy as np

x = np.random.gamma(2,3,100000)

plt.figure()
plt.subplot(221)
plt.hist(x, bins=30)
plt.subplot(222)
plt.hist(x, bins = 30, normed=True)
plt.subplot(223)
plt.hist(x, bins = 30, cumulative=True)
plt.subplot(224)
plt.hist(x, bins = 30, cumulative=True, normed=True, histtype="step")

plt.show()