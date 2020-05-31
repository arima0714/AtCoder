N = int(input())
A = [int(k) for k in input().split()]

import numpy as np
result = np.prod(A)
if (result > 10 ** 18):
    result = -1

print(result)
