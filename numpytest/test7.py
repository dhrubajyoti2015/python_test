

import numpy as np

arr5 = np.array([[11, 2, 3, 4, 5], [6, 17, 28, 9, 90]])
print('sorted array ---',np.sort(arr5, axis=None))

print('sorted array row wise ---',np.sort(arr5, axis=1))

print('sorted array row wise ---',np.sort(arr5, axis=0, kind = 'mergesort'))

