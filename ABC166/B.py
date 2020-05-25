il1 = [int(k) for k in input().split()]
N = il1[0]
K = il1[1]
A = [0] * (N+1)
A[0] = A[0] + 1
for i in range(K):
    d = int(input())
    tmp_A = [int(k) for k in input().split()]
    for a in tmp_A:
        A[a] = A[a] + 1

print(A.count(0))
