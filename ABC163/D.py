# 入力は1行で[数値 数値]
def return_number(n, k):
    return n * k - k*k + k + 1


il1 = input().split()
N = int(il1[0])
K = int(il1[1])

answer = 0
min_ = 0
max_ = 0

for k in range(K, N+2):
    num  = return_number(N, k)
    answer = answer + num

print(answer)
