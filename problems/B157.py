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

for i in b:
    for j in range(3):
        for k in range(3):
            if A[j][k] == i:
                A[j][k] = -1

if (A[0][0] == A[0][1] and A[0][1] == A[0][2] and A[0][2] == -1):
    print("Yes")
elif (A[1][0] == A[1][1] and A[1][1] == A[1][2] and A[1][2] == -1):
    print("Yes")
elif (A[2][0] == A[2][1] and A[2][1] == A[2][2] and A[2][2] == -1):
    print("Yes")
elif (A[0][0] == A[1][0] and A[1][0] == A[2][0] and A[2][0] == -1):
    print("Yes")
elif (A[0][1] == A[1][1] and A[1][1] == A[2][1] and A[2][1] == -1):
    print("Yes")
elif (A[0][2] == A[1][2] and A[1][2] == A[2][2] and A[2][2] == -1):
    print("Yes")
elif (A[0][0] == A[1][1] and A[1][1] == A[2][2] and A[2][2] == -1):
    print("Yes")
elif (A[0][2] == A[1][1] and A[1][1] == A[2][0] and A[2][0] == -1):
    print("Yes")
else:
    print("No")
