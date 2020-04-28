import math
il = input().split()
A = int(il[0])
B = int(il[1])

flag = -1

for i in range(10, 1000+1):
    if(math.floor(i * 0.08) == A and math.floor(i * 0.1) == B):
        flag = i
        break
print(flag)
