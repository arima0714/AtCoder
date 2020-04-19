il = input().split()
N = int(il[0])
K = int(il[1])

old = N
new = 0

a = N // K
b = N % K
c = abs(N - (K * (a+1)))

if (b > c):
    print(c)
else:
    print(b)
