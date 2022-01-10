import numpy as np

arr0 = np.array(42)
print(arr0)

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print("3D array-----")
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)

arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5.ndim)