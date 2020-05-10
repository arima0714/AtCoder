il = [int(k) for k in input().split()]
N = il[0]
K = il[1]
A = [int(k) for k in input().split()]
A.insert(0,0)

k = 0
result = 1

while k < K:
    result = A[result]
    k += 1

print(result)
