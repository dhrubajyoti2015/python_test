import pandas as pd
import numpy as np

#info = pd.DataFrame(np.random.randn(10, 2), columns=['col1', 'col2'])
#print(info)
#for row_index, row in info.iterrows():
    #print('row_index--',row_index,'--row--', row)

df = pd.read_csv("E:/testdata/rakesh/nba.csv")
df2 = df.head(2)
print(df2)

for index,data in df2.iterrows():
    print('index-',index,'--data--',data)