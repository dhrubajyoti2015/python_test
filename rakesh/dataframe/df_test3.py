import pandas as pd

data = [['Axel',32], ['Alice', 26], ['Alex', 45]]
#df = pd.DataFrame(data)
df = pd.DataFrame(data,columns=['Name','Age'])
#print(df)
#print(df['Age'])
print("-----------")

list = [110,111,112]
c = pd.DataFrame(list, columns=['roll_number'])
df['roll'] = c
d = pd.DataFrame(['Delhi','Patna','Warangle'],columns=['location'])
df['location'] = d
print(df)
print("-----------")
del df['roll']
print(df)



