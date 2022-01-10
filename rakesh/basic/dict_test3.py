sq = {1:1,(1,1,1):4,3:9,4:16,5:25}
print(all(sq))

sq = {1:1,2:{"name":"rakesh","age":28},3:(9,10,11),4:16,5:[25,26,27,28]}
print(sq)

sq = {6:36,1:1,3:9,4:16,5:25,2:4}
print(sq)
print(sorted(sq,reverse=True))

print("########################")
sq = {6:36,1:1,3:9,4:16,5:25,2:4}

for i in sorted(sq.keys()):
    print(i,":",sq[i])

d3 = {"a":1,"b":2,"c":3}
d4 = {"d":4,"e":5}
d5 = {"f":6,"g":7}

d3.update(d4)
print(d3)

d6 = d4|d5
print(d6)
print(type(d6))
v = str(d6)
print(type(v))

