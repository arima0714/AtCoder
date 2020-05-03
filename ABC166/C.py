il1 = [int(k) for k in input().split()]
N = il1[0]
M = il1[1]
H = [int(k) for k in input().split()]
result = [True]*N
for m in range(M):
    il = [int(k) for k in input().split()]
    A = il[0]-1
    B = il[1]-1
    if (H[A] < H[B]):
        result[A] = False
    elif (H[A] > H[B]):
        result[B] = False
    else:
        result[A] = False
        result[B] = False

print(result.count(True))
