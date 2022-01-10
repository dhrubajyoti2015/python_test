
set1 = {1,2,3,4,5,6}
print(len(set1))

set1.discard(3)
print(set1)

set2 = {'a','b','c',1,3,5}
print(set2)

set2.discard('b')
print(set2)

set3 = {1,2,3,4,5,6}
set3.remove(4)
print(set3)


set4 = {1,2,3,4,5,6}
set4.discard(8)
print(set4)

set4 = {1,2,3,4,5,6}
set4.remove(8)
print(set4)

set4.clear()
print(set4)

