il = input().split()
N = int(il[0])
A = int(il[1])
B = int(il[2])

result = (N//(A+B)) * A
if(N%(A+B) >= A):
    result = result + A
else:
    result = result + N%(A+B)

print(result)
