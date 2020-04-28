A_1 = input().split()
A_2 = input().split()
A_3 = input().split()
A_1 = [int(k) for k in A_1]
A_2 = [int(k) for k in A_2]
A_3 = [int(k) for k in A_3]
A = []
A.append(A_1)
A.append(A_2)
A.append(A_3)

N = int(input())

b = []
for i in range(N):
    b.append(int(input()))
