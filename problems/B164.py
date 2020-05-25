il = [int(k) for k in input().split()]
A = il[0]
B = il[1]
C = il[2]
D = il[3]

import math

t = math.ceil(C/B)
a = math.ceil(A/D)

if t <= a:
    print("Yes")
else:
    print("No")
