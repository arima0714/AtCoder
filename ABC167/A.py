S = input()
T = input()

if ((S in T[:-1]) and (len(S)+1 == len(T))):
    print("Yes")
else:
    print("No")
