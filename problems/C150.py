N = int(input())
P = ''.join(input().split())
Q = ''.join(input().split())

candidate = []
candidates = []

for i in range(1, N+1):
    candidate.append(str(i))

import itertools
for p in itertools.permutations(candidate, N):
    candidates.append(''.join(p))

candidates.sort()

a = candidates.index(P)
b = candidates.index(Q)

print(str(abs(a-b)))
