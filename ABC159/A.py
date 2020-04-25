input_line = input().split()
N = int(input_line[0])
M = int(input_line[1])

import math

print("N="+str(N)+" M="+str(M))

def combination(n, r):
    return math.factorial(n) / math.factorial(n-r) / math.factorial(r)

print(combination(N,M))
