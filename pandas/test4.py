import pandas as pd

import numpy as np


info1 = np.array(['P','a','n','d','a','s'])
a = pd.Series(info1)
#print(a)

#x = pd.Series()
#print(x)

info2 = {'x': 0, 'y': 1, 'z': 2.50}
a = pd.Series(info2)
#print(a)

x = pd.Series(4, index=[0, 1, 2, 3])
#print(x)

x = pd.Series([1,2,3],index = ['a','b','c'])
#retrieve the first element
print(x)
#print(x[0])