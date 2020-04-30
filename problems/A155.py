il = [int(k) for k in input().split()]

if (il[0] != il[1] and il[1] == il[2]):
    print("Yes")
elif (il[0] != il[1] and il[0] == il[2]):
    print("Yes")
elif (il[0] != il[2] and il[0] == il[1]):
    print("Yes")
else:
    print("No")
