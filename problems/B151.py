il = [int(k) for k in input().split()]
N = il[0]
K = il[1]
M = il[2]
A = [int(k) for k in input().split()]

n = M*N - sum(A)

if (n > K):
    print(-1)
elif (n < 0):
    print(0)
else:
    print(n)
