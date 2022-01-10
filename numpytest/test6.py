import numpy as np

#a = np.array([1,2,3,4])
#add 1 to each element
#print(a+1)

#print(a*4)

#print(a**2)

#a *= 2
#print(a)


arr5 = np.array([[11, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#print('largest element --', arr5.max())
#print('largest element --', arr5.min())
#print('sum of all elements ---',arr5.sum())
#print('sum of each array element ---',arr5.sum(axis=1))

a = np.array([[1,2],[3,4]])
b = np.array([[4,1],[6,2]])

print('sum of arrays --', a+b)
print('multiplication --',a*b)

print('matrix multiplication --',a.dot(b))




