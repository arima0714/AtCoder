N = int(input())
S = input()

ans = S.count("R")*S.count("G")*S.count("B")

for i in range(N-2):
    for j in range(i+1, N-1):
        k = j-i + j
        if k < N and S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
            ans -= 1

print(ans)
