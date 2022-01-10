import pandas as pd

dict = {'name':['u','v','w','x','y','z'],'age':[29,24,22,25,27,19],'marks':[80,75,90,78,82,79]}
#print(dict)
df = pd.DataFrame(dict)
#print(df)
#print(df.head(2))
#print(df.tail(2))
#print(df.iloc[:-2])
#print(df.iloc[-2:])

#print(df.iloc[1:3])
#print(df.iloc[3:5])
print(df[-3:])

