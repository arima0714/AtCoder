# 入力は1行で[数値 数値]

il1 = input().split()
N = int(il1[0])+1
K = int(il1[1])

list = [1]
for i in range(1,N+1):
    list.append(list[-1] * i)

answer = 0

for k in range(K, N+1):
    print("N= "+str(N)+" N-k= "+str(N-k)+" k= "+str(k))
    answer = answer + list[N] / (list[N-k] * list[k])

print(answer)
print(list)

def return_number(max, min):
    return max-min+1

def return_max(n, k):
    ans = 0
    for i in range(k):
        ans = ans + n - k
    return ans

def return_min(n, k):
    ans = 0
    for i in range(k):
        ans = ans + k
    return ans
