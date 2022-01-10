#a = "welcome to python"
a ="Welcome"
print(a)
print(a[0])
print(a[-1])
print(len(a))

print(a[0:3])

b = "welcome to python"
print(b[0:7])

list = []
print(list)

list1 = ["python"]
print(list1)

list2 = ["python","easy","to","learn"]
print(list2)

list3 = ["Hello", "python", 3,["python","java"]]
print(list3)

print(list3[3][1])

list4 = ["Hello", "python", 3,["python",[99,100,200.50],"java"]]
print(list4)

print(list4[3][1][1])

print(len(list4))

list4.append("123")
print(list4)

list4.insert(1,"Tuesday")
print(list4)

#list4.clear()
#print(list4)

#list4.remove("Tuesday")
#print(list4)

#list4.pop(3)
#print(list4)

list1 = [1,2,3,4,5,6,7]
print(list1[0:3])

list1.reverse()
print(list1)

list5 = [1,2,3,4,5,6,7]
#list5.clear()
print(list5)

del list5[0:3]
print(list5)


list7 = [11,2,30,4,5,60,7]
list7.sort(reverse=True)
print(list7)

for i in list7:
    print(i)