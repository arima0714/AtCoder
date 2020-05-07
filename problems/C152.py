N = int(input())
P = [int(k) for k in input().split()]

result = 0
for i in range(N):
    for j in range(0,i):
        # j < i
        if P[i] > P[j]:
            result = result - 1
            break

print(N+result)
