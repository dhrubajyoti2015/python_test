import numpy as np

#arr = np.array([1, 2, 3, 4])
arr = np.array([[1, 2, 3],[2, 5, 3]])
#print(arr)
#print(arr[1][1])

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3)

print(arr3[1, 1, 0])

#2 array elements -- 2 array elements -- 3 elements

arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr4[0, -2])
