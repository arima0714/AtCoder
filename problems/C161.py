il = input().split()
N = int(il[0])
K = int(il[1])

old = N
new = 0

while True:
    new = abs(old - K)
    print("old = " + str(old) + " new = " + str(new))
    if(old > new):
        old = new
    else:
        break

print(old)
