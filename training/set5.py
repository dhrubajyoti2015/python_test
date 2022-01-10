
x = {"a","b","c","d","e"}
y = {"b","c"}
z = {"c","d"}
print(x.difference(y))

#union
x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
print(x.union(y))

#intersection
x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
print(x.intersection(y))

print("###########")
#difference update
x = {"a","b","c","d","e"}
y = {"b","c"}
#print(x.difference_update(y))
x.difference_update(y)
print(x)

x = {"a","b","c","d","e"}
y = {"b","c"}
x = x - y
print(x)

