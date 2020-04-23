# 入力は1行で[数値 数値]
def return_number(max, min):
    return max-min+1

def return_max(n, k):
    ans = 0
    for i in range(k):
        ans = ans + n - i
        # print("ans= "+str(ans)+" i= "+str(i))
    return ans

def return_min(n, k):
    ans = 0
    for i in range(k):
        ans = ans + i
    return ans

il1 = input().split()
N = int(il1[0])
K = int(il1[1])

answer = 0
min_ = 0
max_ = 0

for k in range(K, N+2):
    min_ = return_min(N,k)
    max_ = return_max(N,k)
    num  = return_number(max_, min_)
    # print("k= "+str(k)+" N= " +str(N)+" min= "+str(min_)+" max= "+str(max_)+" num= "+str(num))
    answer = answer + num

print(answer)
