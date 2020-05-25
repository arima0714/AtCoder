il = [int(k) for k in input().split()]
A = il[0]
B = il[1]
for i in range(B):
    if i * A - i + 1 >= B:
        print(i)
        break
