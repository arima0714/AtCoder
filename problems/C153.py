il1 = [int(k) for k in input().split()]
N = il1[0]
K = il1[1]
H = [int(k) for k in input().split()]

H.sort(reverse=True)

if len(H) <= K:
    counter = len(H)
else:
    counter = K

for k in range(counter):
    H[k] = 0

S = sum(H)

print(S)
