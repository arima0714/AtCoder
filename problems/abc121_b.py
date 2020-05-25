il = [int(k) for k in input().split()]
B = [int(k) for k in input().split()]
N = il[0]
M = il[1]
C = il[2]
result = 0

for i in range(N):
    A = [int(k) for k in input().split()]
    tmp_list = [x * y for (x, y) in zip(A, B)]
    sum_tmp_list = sum(tmp_list)
    if sum_tmp_list + C > 0:
        result += 1

print(result)
