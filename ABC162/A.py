input_n = input()

flag = True

for char in input_n:
    if char == "7":
        print("Yes")
        flag = False
        break

if flag == True:
    print("No")
