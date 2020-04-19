il1 = input().split()
il2 = input().split()

il1 = [int(i) for i in il1]
il2 = [int(i) for i in il2]

N = il1[0]
M = il1[1]

A = il2

for a in il2:
    N = N - a

if N >= 0:
    print(N)
else:
    print(-1)
