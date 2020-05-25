N = int(input())
X = [int(i) for i in input().split()]

X.sort()
X_min = X[0]
X_max = X[N-1]

result = -1
total = 0
for P in range(X_min, X_max+1):
    for x in X:
        total = total + (x-P)**2
    if (total < result or result < 0):
        result = total
    elif (total > result):
        break
    total = 0
print(result)
