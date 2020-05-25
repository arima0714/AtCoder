N = int(input())
A = [int(k) for k in input().split()]

result = True

# for char in A:
#     if(A.count(char) != 1):
#         result = False
#         break
# for i in range(N):
#     for j in range(i+1, N):
#         # print("A[i]= "+str(A[i])+", A[j]= "+str(A[j]))
#         if A[i] == A[j]:
#             result = False
A.sort()

for i in range(N-1):
    if (A[i] == A[i+1]):
        result = False
        break

if (result == True):
    print("YES")
else:
    print("NO")
