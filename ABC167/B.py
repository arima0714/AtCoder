il = [int(k) for k in input().split()]

A = il[0]
B = il[1]
C = il[2]
K = il[3]

if (K <= A):
    print(K)
elif (K <= A+B):
    print(A)
else:
    print( A - (K-(A+B)) )
