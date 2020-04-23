il1 = input().split()
N = int(il1[0])
K = int(il1[1])

list = [1]
for i in range(1,N+1):
    list.append(list[-1] * i)

print(list)
print("N= "+str(N)+" K= "+str(K))