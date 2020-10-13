N = int(input())
a_i = [int(a) for a in input().split()]
a_i.insert(0, 0)

result = 0

for i in range(len(a_i)):
    if(a_i[i] == 0):
        pass
    elif (a_i[a_i[i]] == i):
        result+=1
        a_i[a_i[i]] = 0
        a_i[i] = 0

print(result)
