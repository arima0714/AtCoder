N = int(input())
a = [int(k) for k in input().split()]
a.sort(reverse = True)
sub = 0

for i in range(N//2):
    sub += a[2*i] - a[2*i +1]
if (N%2 == 1):
    sub += a[-1]

print(sub)
