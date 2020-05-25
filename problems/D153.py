H = int(input())
import math

h = H
enemies = 0
counter = 0

while h >= 1:
    counter = counter + 1
    h = h//2

print(2**counter - 1)
