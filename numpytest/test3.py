import numpy as np


a = np.array([[1,2,3],[4,5,6]],dtype='float')
#print('array from list --', a)

b = np.array((1,2,3))
#print('array from tuple --', b)

c = np.zeros((3,4))
#print('array with 3X4 --',c)

d = np.full((2,2),4, dtype='float')
print('array with all 6s --',d)

e = np.random.random((2,2))
#print('random ---',e)

f = np.arange(0,40,5)
#print('array using sequence --',f)



