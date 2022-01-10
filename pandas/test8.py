
import pandas as pd
import numpy as np
#info=pd.DataFrame([[1,5,7],[10,12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['X','Y','Z'])
info=pd.DataFrame([[1,5,7],[10,12,15],[18,21,24]],columns=['X','Y','Z'])
print(info)
info2 = info.agg(['sum','max'])
#print(info2)
print("---------------------")
#df = info.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
#print(df)

#print(info2.count())


info = pd.DataFrame({"Person":["Parker", "Smith", "William", "John"],  "Age": [27., 29, 40, 32]})
print(info.count(axis='columns'))
print("---------------------")
emp = {"Name": ["Parker", "Smith", "William", "Parker"],  "Age": [21, 32, 29, 21]}
info = pd.DataFrame(emp)
print(info)
info = info.drop_duplicates()
print(info)