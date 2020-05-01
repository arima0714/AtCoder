N = input()
A = [int(k) for k in input().split()]

result = True

for char in A:
    if(A.count(char) != 1):
        result = False
        break

if (result == True):
    print("YES")
else:
    print("NO")
