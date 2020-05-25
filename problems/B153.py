il1 = [int(k) for k in input().split()]
A = [int(k) for k in input().split()]
H = il1[0]
N = il1[1]

tmp = H
for a in A:
    H = H - a

if H <= 0:
    print("Yes")
else:
    print("No")
