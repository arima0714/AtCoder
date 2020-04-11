# 入力は１行で[数値 数値 数値]の計３つの数値がスペース区切りで渡される

input_line = input().split()

answer = 0

for i in range(int(input_line[0]) + 1) :
    tmp = 0
    for j in list(str(i)):
        tmp = tmp + int(j)
    if int(input_line[1]) <=  tmp <= int(input_line[2]) :
        print("tmp = ", i)
        answer = answer + i
        
print(answer)
