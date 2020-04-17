# 入力は一行のみで[数値1 数値2]の形式

input_line = input().split()
input_line = [int(s) for s in input_line]

loop = True

x = -1
y = -1
z = -1

for i in range(input_line[0]+1):
    for j in range(input_line[0]+1):
        k = input_line[0] - i -j
        if( k < 0):
            break
        elif(input_line[1] == 10000 * i + 5000 * j + 1000 * k and i + j + k == input_line[0]):
            loop = False
            x = i
            y = j
            z = k
    if (loop == False):
        break

print(str(x) +" "+ str(y) +" "+ str(z))
