
m = 100
n = 0
#print(m/n)

try:
    m = 100
    n = 0
    c = m/n
except ZeroDivisionError:
    print("division by zero")