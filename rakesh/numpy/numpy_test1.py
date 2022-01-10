import numpy
import numpy as np

print("hello numpy")

a = np.array
print(a)

b = numpy.array([1,2,3])
print(b)

c = numpy.array([[[1,2,3],[4,5,6],[1,51,61]]])
print(c)

print("dimension---",c.ndim) ##

a = np.array([[1,2,3]])
print(a)
print("dimension---",a.ndim)
print("data type ---",a.dtype)

d = np.array([[1,2,3,4,5,6]])
print("size --",d.size)
print("shape --",d.shape)

e = np.array([[1,2],[3,4],[5,6]])
print("original --",e)

f = e.reshape(2,3)
print("reshaped --",f)
print("##########")
g = np.array([[1,2,9],[3,4,5],[15,16,19]])
print(g)
#4,19
print(g[1,1],"--",g[2,2])
#print(g[2,0])


a = np.array([1,2,5,6,8,9,10])
print("array --",a)
print("maximum value --",a.max())
print("minimum value --",a.min())
print("sum of elements --",a.sum())


