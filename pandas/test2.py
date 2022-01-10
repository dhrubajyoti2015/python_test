
import pandas as pd

df = pd.DataFrame()
print(df)

data1 = [1,2,3,4,5]
df1 = pd.DataFrame(data1)
print(df1)

data2 = [['A',10],['B',20],['C',30]]
df2 = pd.DataFrame(data2, columns=['name','age'])
print(df2)

data3 = {'name':['a','b','c','d'],'age':[20,22,25,19]}
df3 = pd.DataFrame(data3)
print(df3)


