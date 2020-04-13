# 入力は一行のみで[数値]
import math

input_num = int(input())


sum = 0

for i in range(input_num):
    i = i+1
    for j in range(input_num):
        j = j+1
        for k in range(input_num):
            k = k+1
            sum = sum + math.gcd(math.gcd(i,j),k)

print(sum)
