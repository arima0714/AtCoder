il1 = input().split()
il2 = [int(k) for k in input().split()]
S = il1[0]
T = il1[1]
A = il2[0]
B = il2[1]
U = input()
if (S.find(U) >= 0):
    A = A-1
if (T.find(U) >= 0):
    B = B-1
print(str(A) + " " + str(B))
