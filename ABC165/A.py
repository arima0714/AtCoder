K = int(input())
il2 = [int(k) for k in input().split()]
A = il2[0]
B = il2[1]

result = False

for i in range(A, B+1):
    if (i%K==0):
        result = True
        break

if (result):
    print("OK")
else:
    print("NG")
