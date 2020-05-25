il =[int(k) for k in input().split()]
H = il[0]
A = il[1]

ans, mod = divmod(H, A)

if mod == 0 :
    print(ans)
else:
    print(ans + 1)
