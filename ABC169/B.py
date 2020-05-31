N = int(input())
A = [int(k) for k in input().split()]

result = 1

border = 10 ** 18

for i in A:
    if result == 0:
        break
    result = result * i

if result > border:
    result = -1

print(result)
