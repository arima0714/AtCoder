N = int(input())
P = [int(k) for k in input().split()]

maxes = []
mins  = []

max = 0
min = 0
result = 0

for i in range(N):
    if i == 0:
        max = P[i]
        min = P[i]
    else:
        if(max < P[i]):
            max = P[i]
        if(min > P[i]):
            min = P[i]

    maxes.append(max)
    mins.append(min)

for i in range(N):
    if mins[i] == P[i]:
        result = result + 1

print(result)
