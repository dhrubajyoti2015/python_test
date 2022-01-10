
import pandas as pd

data = [{'a':10, 'b':15},{'a':12, 'b':25,'c':18}]
df = pd.DataFrame(data)
print(df)

data = [{'a':10, 'b':15,'c':20},{'a':12, 'b':25,'c':18}]
df = pd.DataFrame(data)
print(df)

data = [{'a':10, 'b':15,'c':20},{'a':12, 'b':25,'c':18}]
df = pd.DataFrame(data,index =['first','second'])
print(df)