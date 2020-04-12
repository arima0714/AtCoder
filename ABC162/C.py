# 入力は一行のみで[数値]

input_num = int(input())

import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

print(gcd(27, 18, 9))
