
import pandas as pd
import numpy as np
info1 = np.array(['p','a','n','d','a','s'])
a = pd.Series(info1)
print(a)


info2 = {'x': 0.0, 'y': 1.0, 'z': 2.0}
b = pd.Series(info2)
print(b)