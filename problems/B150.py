N = int(input())
S = input()

result = 0

for n in range(N):
    if S[n:n+3] == "ABC" :
        result += 1

print(result)
    