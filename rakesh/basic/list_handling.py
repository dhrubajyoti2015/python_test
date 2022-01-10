

l1 = [1,2,3,4]
print(l1)

l2 = [1,2,"abcd",1.55,'hello',True]
print(l2)

for each in l2:
    print(each)

l3 = [1,2,"abcd",1.55,'hello',True,[3,4,5]]
print(l3)

print(l3[2])

l4 = [1,2,3,4,5,"abcd"]
print(l4)
l4.append("xyz")
print(l4)

print(l4.index("abcd"))

#index = l4.index("abcd1")
#print("index of abcd1 --",index)

l5 = [10,2,5,7,19]
l5.sort()
print(l5)

l5.sort(reverse=True)
print(l5)

l6 = [10,2,5,7,19]
l6.insert(0,'wonderful')
print(l6)

l6.remove('wonderful')
print(l6)

l7 = [1,3,5,3,3,6,7,1,1,1,7,10,9,2]
count = l7.count(1)
print('count---',count)

l8 = [10,2,5,7,19]
l8.pop(0)
print(l8)

l9 = ['java','python','c#','C++','SQL']
print(l9)
#l9.pop()

#remove last value
#l9.pop(-1)
#print(l9)

#l9.pop(-4)
#l9.pop(2)
print(l9)



#length
print("length----",len(l9))

l10 = [1,2,'python','c#','C++',3,5,6]
l10.reverse()
print(l10)

l11 = [1,2,3,4,[5,6,7,8],True,'Python']
print(l11[4][3])

print(type(l11))


l11 = [1,2,3,4,[5,6,7,8],True,'Python']
l12 = ['java','bigdata','Python']
print(l11+l12)
print(l11.__add__(l12))







