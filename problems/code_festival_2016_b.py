il = [int(k) for k in input().split()]
S = input()
N = il[0]
A = il[1]
B = il[2]

S = "z"+S

passed = 0
passed_oversea = 0

for i in range(len(S)):
    if S[i] == "a":
        if passed < A+B:
            passed += 1
            print("Yes")
        else:
            print("No")
    elif S[i] == "b":
        passed_oversea += 1
        if passed < A+B and passed_oversea <= B:
            passed += 1
            print("Yes")
        else:
            print("No")
    elif S[i] == "c":
        print("No")
