# 入力は一行のみで[数値]

input_num = int(input())

def gcd(*numbers):
    return reduce(math.gcd, numbers)

import math
from functools import reduce

memory = {}
tmp_str = ""
tmp_list = [0, 0, 0]

sum = 0

for i in range(input_num):
    i = i+1
    for j in range(input_num):
        j = j+1
        for k in range(input_num):
            k = k+1
            tmp_list[0] = i
            tmp_list[1] = j
            tmp_list[2] = k
            tmp_list.sort
            tmp_str = str(tmp_list)
            if(memory.get(tmp_str) == None):
                memory[tmp_str] = gcd(i,j,k)
            sum = sum + memory[tmp_str]

print(sum)
