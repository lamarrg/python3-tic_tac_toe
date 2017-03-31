import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(size=1000)

plt.hist(x, normed=True, bins=np.linspace(-5,5,21)) # bins could also have just an integer. BUT... to get the number of wanted bins, will need to go one higher. to create a single bin, you need a starting point and and end point, etc... 

plt.show()