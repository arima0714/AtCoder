il1 = input().split()
il2 = input().split()

K = int(il1[0])
N = int(il1[1])
A = [int(i) for i in il2]

import time
import copy

fixed_A = copy.copy(A)

for i in A:
    fixed_A.append(i+K)
    print(fixed_A)
    time.sleep(1)

print(fixed_A)
