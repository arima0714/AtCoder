input_line = input().split()
N = int(input_line[0])
M = int(input_line[1])

import math

def combination(n, r):
    if(n == 1 or n == 0):
        return 0
    else:
        return math.factorial(n) // math.factorial(n-r) // math.factorial(r)

print(combination(N,2) + combination(M,2))
