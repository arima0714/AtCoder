H = int(input())
import math
h = H
counter = 0
if h <= 1:
    counter = counter + 1
while h > 1 :
    counter = counter+1
    h = math.floor(h/2)
if H > 1:
    pass

print(counter)
