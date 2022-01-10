
square = {1:1,2:4,3:9,4:16}
print(square)

#remove
#square.pop(2)
#print(square)

#square.clear()
#print(square)

#del square
#print(square)

print(square.keys())

print(square.items())

print(square.values())

square2 = {1:1,2:4,3:9,4:16,5:25}
#print(square2.popitem())

#for each in square2:
    #print(each)

for eachKey in square2.keys():
    print(eachKey)

for eachValue in square2.values():
    print(eachValue)

#test = {'1':"one", 1:"One","name":['abc','xyz','mno']}
#print(test)

#test = {'1':"one", 1:"One",[1,2,3]:['abc','xyz','mno']}
#print(test)

test = {'1':"one", 1:"One",(1,2,3):['abc','xyz','mno']}
print(test)

print(len(test))

square3 = {6:36,1:1,2:4,3:9,4:16}
print(square3.keys())
sorted_sqaure3 = sorted(square3)
print(sorted_sqaure3)

sorted_sqaure_desc = sorted(square3, reverse=True)
print(sorted_sqaure_desc)

