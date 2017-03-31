import numpy as np

z1 = np.array([1,3,5,7,9])

z2 = z1 + 1

print(z2)

ind = [0,2,3]  # this is the positions to be indexed
# can also be defined as np array -> np.array([0,2,3])

print(z1[ind])

#---------------


print(z1 > 6) # iterates over each item of the array and does the comparison

print(z1[z1 > 6]) # Returns results in an array form that meet the conditions

# if you do a slice (returns a view) instead of an index (returns copy of original data), you can change the value of the referenced list...

# This will be ok...
# w = z1[ind]
# w[0] = 3
# print(z1)

# This will not
w = z1[0:3]
w[0] = 3
print(z1)