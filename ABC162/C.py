# 入力は一行のみで[数値]

input_num = int(input())

def gcd(*numbers):
    return reduce(math.gcd, numbers)

import math
from functools import reduce

sum = 0

for i in range(input_num):
    i = i+1
    for j in range(input_num):
        j = j+1
        for k in range(input_num):
            k = k+1
#            print("i = "+str(i)+" j = "+str(j)+" k = "+str(k)+" gcd() = "+str(gcd(i,j,k)))
            sum = sum + gcd(i, j, k)

print(sum)
