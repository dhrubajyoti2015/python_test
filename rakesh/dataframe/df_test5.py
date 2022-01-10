import pandas as pd
import numpy as np
info=pd.DataFrame([[1,5,7],[10,12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['X','Y','Z'])
print(info)
print(info.agg(['sum','min'])) #colunwise

info1 = pd.DataFrame([[1,5,7],[10,12,15],[18,21,24],[np.nan,np.nan,np.nan]],columns=['X','Y','Z'])
#print(info1)
#df = info1.agg({'A': ['sum', 'min'], 'B': ['min', 'max']})
#print(df)