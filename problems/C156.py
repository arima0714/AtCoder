N = int(input())
X = [int(i) for i in input().split()]

X.sort()
X_min = X[0]
X_max = X[N-1]

print("x_min="+str(X_min)+" x_max="+str(X_max))
