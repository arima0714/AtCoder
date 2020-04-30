N = int(input())
A = [int(k) for k in input().split()]

result = "APPROVED"

for x in A:
    if (x%2 == 0):
        if(x%3 == 0 or x%5 == 0):
            pass
        else:
            result = "DENIED"
            break

print(result)
