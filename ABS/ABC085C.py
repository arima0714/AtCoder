# 入力は一行のみで[数値1 数値2]の形式

input_line = input().split()
input_line = [int(s) for s in input_line]

x = -1
y = -1
z = -1

tmp = input_line[1]

x, tmp = divmod(tmp, 10000)
y, tmp = divmod(tmp, 5000)
z, tmp = divmod(tmp, 1000)

print(str(x) +" "+ str(y) +" "+ str(z))