import math

il = [int(k) for k in input().split()]
A = il[0]
B = il[1]
H = il[2]
M = il[3]

h = ((H + (M/60))/12) * 360
m = (M/60) * 360

k = abs(h-m)

# print("k = "+str(k))

if k > 180:
    k = 360 - k

radian = math.radians(k)

resut = math.sqrt(A**2 - 2*A*B*math.cos(radian) + B**2)
print(resut)
