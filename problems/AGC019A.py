il = [int(i) for i in input().split()]
N = int(input())

Q = il[0]
H = il[1]
S = il[2]
D = il[3]

single = min([Q*4, H*2, S])
double = min([single*2, D])

result = (N//2) * double + (N%2) * single

print(int(result))
