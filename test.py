# a = [[1,2],[2,3]]
# del a[0]
# print(a[0])

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

a = np.delete(a, 0, 1)
print (a[0])