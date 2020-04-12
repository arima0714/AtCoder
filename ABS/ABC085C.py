# 入力は一行のみで[数値1 数値2]の形式

input_line = input().split()
input_line = [int(s) for s in input_line]

loop = True

for i in range(input_line[0]):
    for j in range(input_line[0]):
        k = input_line[0] - i -j
        if(input_line[1] == 10000 * i + 5000 * j + 1000 * k and i + j + k == input_line[0]):
            print(str(i) +" "+ str(j) +" "+ str(k))
            loop = False
    if (loop == False):
        break
