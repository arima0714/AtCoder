il = [int(i) for i in input().split()]
N = int(input())

Q = il[0]
H = il[1]
S = il[2]
D = il[3]

QList = [Q, 0.25/Q, 0.25]
HList = [H, 0.5/H, 0.5]
SList = [S, 1.0/S, 1.0]
DList = [D, 2.0/D, 2.0]

XList = [QList, HList, SList, DList]

XList = sorted(XList, reverse = True, key=lambda x: x[1])

rest = N
result = 0
for x in XList:
    if[x[2] <= rest]:
        x_n = rest//x[2]
        if(x_n != 0):
            rest = rest - x[2] * x_n
            result = result + x_n * x[0]
print(int(result))
