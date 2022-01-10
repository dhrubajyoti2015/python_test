
t1 = (1,2,3,'python',True,[1,2,3,4],99)
print(t1)

for each in t1:
    print(each)

print(t1[0:3])
print(t1[:3])
print(t1[1:6])

t2 = (1,2,3,4,'python',True,[1,2,3,44],99,100,111,112)
print(t2[0:11:2])

print(t2.index(111))
print(len(t2))

print(t2[6][3])

t3 = (1,2,66,55,99,11,22)
print("max value --",max(t3))
print("min value --",min(t3))

print(type(t3))

t4 = (1,2,66,55,99,11,22)
t4_sorted = sorted(t4)
print(t4_sorted)

t4_sorted_rev = sorted(t4, reverse=True)
print(t4_sorted_rev)



