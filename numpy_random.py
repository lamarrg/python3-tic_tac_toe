import numpy as np
import matplotlib.pyplot as plt

np.random.random()

#np.random.random(5)  -->> insterting a number into thr method will generate an array of that many items

# np.random.random((2,3)) -->> to do a 2D array, enter the number of rows and columns in a tuple

# --------
# np.random.normal(0,1,5)
#
# np.random.normal(0,1, (2,5)) # the tuple at the end allows you to create a 2D array, specifiying number of rows and columns
# --------

X = np.random.randint(1,7,(1000000,10))
Y = np.sum(X, axis=1)
plt.hist(Y);
plt.show()