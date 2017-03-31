import numpy as np

x = np.array([1,2,3])
y = np.array([2,4,6])

X = np.array([[1,2,3],
              [4,5,6]])

Y = np.array([[2,4,6],
              [8,10,12]])

print(x+y)

print(X[:,1])

print(X[:,1] , Y[:,1])
print(X[:,1] + Y[:,1])