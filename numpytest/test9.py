import numpy as np
import pandas as pd

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

#print(arr.shape)

arr2 = np.array([1, 2, 3, 4], ndmin=3)
#print(arr2)
#print('shape of array :', arr2.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#print(arr)
#newarr = arr.reshape(3, 4)
#print(newarr)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

