import pandas as pd

df1 = pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
df2 = pd.DataFrame([[5,6],[7,8]],columns=['a','b'])

#append
df1 = df1.append(df2)
print(df1)
print("#################")
#deletion
df1 = df1.drop(0)
print(df1)



