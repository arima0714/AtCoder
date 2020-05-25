il = [int(k) for k in input().split()]
N = il[0]
K = il[1]
A = [int(k) for k in input().split()]
A.insert(0,0)
visited = [-1]*(N+1)

##### ループをしない場合

# k = 0
# result = 1


#### ループをする場合

k = 0
alpha = 0
result = 1
loop_length = 0
while True:
    if (visited[result] < 0):
        visited[result] = k
        result = A[result]
        k += 1
    else:
        alpha = visited[result]
        loop_length = k - visited[result]
        break

num = (K-alpha)%(loop_length)
print(num)

while num >= 0:
    result = A[result]
    num -= 1
    print(result)
