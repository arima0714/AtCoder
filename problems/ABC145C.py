import itertools
import math

N = int(input())
il_list = []
for n in range(N):
    il = [int(k) for k in input().split()]
    il_list.append(il)

il_list_perm = itertools.permutations(il_list, len(il_list))

length = 0
counter = 0

for perm in il_list_perm:
    for i in range(len(perm)):
        if (i != 0):
            length = length + math.sqrt((perm[i][0] - perm[i-1][0])**2 + (perm[i][1] - perm[i-1][1])**2)
    counter = counter + 1

print(length/counter)