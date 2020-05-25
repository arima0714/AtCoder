N = int(input())
import math
X = math.ceil(N/1.08)
if math.floor(X * 1.08) == N:
    print(X)
else:
    print(":(")
