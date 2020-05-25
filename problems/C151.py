il1 = [int(k) for k in input().split()]
N = il1[0]
M = il1[1]
answered = ['WA']
answered = answered * (N+1)
result = [0, 0]
was = [0]
was = was * (N+1)

for i in range(M):
    il = input().split()
    p = int(il[0])
    s = il[1]
    if (answered[p] == 'AC'):
        pass
    else:
        if (s == 'AC'):
            result[0] = result[0]+1
            answered[p] = s
            result[1] = result[1]+was[p]
        else:
            was[p] = was[p] + 1

print(str(result[0])+" "+str(result[1]))
