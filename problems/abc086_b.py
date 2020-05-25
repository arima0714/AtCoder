il = input().split()
a = il[0]
b = il[1]

if b[-1] == 2 or b[-1] == 3 or b[-1] == 7 or b[-1] == 8 :
    print("No")
else:
    import math
    N = int(a+b)
    N_2 = math.floor(math.sqrt(N))
    if(N_2 ** 2 == N):
        print("Yes")
    else:
        print("No")
        